import socket
import rsa
import RSAbase
#Generate rsa key(1024 bits)
pubkey, privkey = rsa.newkeys(1024)

#bind socket port - 10013
sk = socket.socket()
sk.bind(('127.0.0.1', 10013))
sk.listen(1)

while True:
    client, addr = sk.accept()
    # send NC pubkey to DNC device
    client.sendall(RSAbase.encode_pubkey(pubkey))
    # fetch MES pubkey from DNC device
    MESpubkey = RSAbase.gen_pubkey(RSAbase.rsa_decry(client.recv(102400), privkey))
    print("NC pubkey sended. \n Acquired MES pubkey: ",MESpubkey)
    # receiving code from DNC
    # code struct = (RSA encrypted code + 128 bits signed signature
    print("Recieving code....")
    Received = client.recv(102400)
    # seperate code = Codepart + Signaturepart
    CodePart = Received[:-128]
    SignaturePart = Received[-128:]
    CodePart = RSAbase.rsa_decry(CodePart, privkey)
    # Decrypt code, verify signature and confirm sender identity
    try :
        print("Signature is ", SignaturePart)
        SignaturePart = rsa.verify(message=CodePart.encode('utf8'), signature=SignaturePart, pub_key=MESpubkey)
        print("Signature confirmed. Content = \n\t%s" % CodePart)
    except :
        print("Signature illegal!")
    break