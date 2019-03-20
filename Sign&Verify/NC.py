import socket
import rsa
import RSAbase

pubkey, privkey = rsa.newkeys(1024)

sk = socket.socket()
sk.bind(('127.0.0.1', 10013))
sk.listen(1)
while True:
    client, addr = sk.accept()
    client.sendall(RSAbase.encode_pubkey(pubkey))
    MESpubkey = RSAbase.gen_pubkey(RSAbase.rsa_decry(client.recv(102400), privkey))
    print("NC pubkey sended. \n Acquired MES pubkey: ",MESpubkey)
    print("Recieving code....")
    Received = client.recv(102400)
    CodePart = Received[:-128]
    SignaturePart = Received[-128:]
    CodePart = RSAbase.rsa_decry(CodePart, privkey)
    try :
        print("Signature is ", SignaturePart)
        SignaturePart = rsa.verify(message=CodePart.encode('utf8'), signature=SignaturePart, pub_key=MESpubkey)
        print("Signature confirmed. Content = \n\t%s" % CodePart)
    except :
        print("Signature illegal!")