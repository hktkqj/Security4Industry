import socket
import rsa
import RSAbase
import random
import string


def generate_random_str(len) :
    set = string.ascii_letters
    str = []
    for i in range(0,len) :
        str.append(random.choice(set))
    return ''.join(str)


pubkey, privkey = rsa.newkeys(1024)
id = "fe80::1004:4946:eb18:754%19"
NCCode = generate_random_str(1000)
print("Generated code: \n\t%s" % NCCode)

sk = socket.socket()
sk.connect(('127.0.0.1', 10012))
sk.sendall(RSAbase.encode_pubkey(pubkey))
sk.sendall(rsa.sign(id.encode('utf8'), priv_key=privkey, hash_method='SHA-256'))
NCpubkey = RSAbase.gen_pubkey(RSAbase.rsa_decry(sk.recv(102400), privkey))
print("NC pubkey received! --\n\t",NCpubkey)
print("Preparing sending Code....\nGenerating signature...")
CodeSignature = rsa.sign(NCCode.encode("utf8"), privkey, hash_method='SHA-256')
CodeEncry = RSAbase.rsa_encry(NCCode, NCpubkey)
SendContent = CodeEncry + CodeSignature
print("Signature (len:%d): " % len(CodeSignature),"\n\t", CodeSignature)
sk.sendall(SendContent)