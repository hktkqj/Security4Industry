import socket
import rsa
import RSAbase

# generate DNC keys
pubkey, pirvkey = rsa.newkeys(1024)
# kept MES's MAC address for signature verify
recorded_MESid = "fe80::1004:4946:eb18:754%19"

# fetch NC pubkey from NC device (from localhost:10013)
ncsk = socket.socket()
ncsk.connect(('127.0.0.1', 10013))
recv_bytes = ncsk.recv(102400)
NCpubkey = RSAbase.gen_pubkey(recv_bytes.decode('utf8'))
print("NC pubkey acquired! --\n\t", NCpubkey)

# listen localhost:10012 from MES
sk = socket.socket()
sk.bind(('127.0.0.1', 10012))
sk.listen(1)
while True :
    client, addr = sk.accept()
    print("New connection from MES", client)
    # receive MES pubkey
    recv_bytes = client.recv(102400)
    MESpubkey = RSAbase.gen_pubkey(recv_bytes.decode('utf8'))
    # receive MES signature
    signature = client.recv(102400)
    # try to verify MES signature
    try :
        rsa.verify(recorded_MESid.encode('utf8'), signature=signature, pub_key=MESpubkey)
        # Successfully verified - send NC pubkey(Encrypted with MES pubkey):
        print("Identity verified ! Sending NC pubkey...")
        client.sendall( RSAbase.rsa_encry( RSAbase.encode_pubkey(NCpubkey).decode('utf8'), MESpubkey) )
        # After verified MES's identity,send MES pubkey to  NC device
        ncsk.sendall( RSAbase.rsa_encry( RSAbase.encode_pubkey(MESpubkey).decode('utf8'), NCpubkey) )
        # receive Product code from MES device, retransmit to NC device
        print("Now receiving code...")
        Receiced_code = client.recv(102400)
        ncsk.sendall( Receiced_code )
        print("Transmitting....transmit length: %d" % len(Receiced_code))

    # except : throw verify failed
    except :
        print("Verify failed!")
    client.close()
    break