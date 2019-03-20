import socket
import rsa
import RSAbase

pubkey, pirvkey = rsa.newkeys(1024)
recorded_MESid = "fe80::1004:4946:eb18:754%19"


ncsk = socket.socket()
ncsk.connect(('127.0.0.1', 10013))
recv_bytes = ncsk.recv(102400)
NCpubkey = RSAbase.gen_pubkey(recv_bytes.decode('utf8'))
print("NC pubkey acquired! --\n\t", NCpubkey)

sk = socket.socket()
sk.bind(('127.0.0.1', 10012))
sk.listen(1)
while True :
    client, addr = sk.accept()
    print("New connection from ", client)
    recv_bytes = client.recv(102400)
    MESpubkey = RSAbase.gen_pubkey(recv_bytes.decode('utf8'))
    signature = client.recv(102400)
    try :
        rsa.verify(recorded_MESid.encode('utf8'), signature=signature, pub_key=MESpubkey)
        print("Identity verified ! Sending NC pubkey...")
        client.sendall( RSAbase.rsa_encry( RSAbase.encode_pubkey(NCpubkey).decode('utf8'), MESpubkey) )
        ncsk.sendall( RSAbase.rsa_encry( RSAbase.encode_pubkey(MESpubkey).decode('utf8'), NCpubkey) )
        print("Now receiving code...")
        Receiced_code = client.recv(102400)
        ncsk.sendall( Receiced_code )
        print("Transmitting....transmit length: %d" % len(Receiced_code))
    except :
        print("Verify failed!")
    client.close()
    break