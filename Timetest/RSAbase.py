import rsa
# This RSAbsae file is made for 1024-bits RSA encryption
# 1024-bit info:
#   len(str) >= 100 : divide blocks


# Input: string, (A public key class) Return: encoded('utf-8') bytes
# Update: Divide blocks for long string
def rsa_encry(d_str,key_in) :
    if len(d_str) > 100 :
        out = b""
        for i in range(0,len(d_str),100) :
            if i+100 >= len(d_str) :
                out = out + rsa_encry(d_str[i:], key_in)
            else :
                out = out + rsa_encry(d_str[i:i+100], key_in)
        return out
    else :
        content = d_str.encode('utf-8')
        return rsa.encrypt(content,key_in)

#Input: bytes, (A private key class) Return: decoded string
#Update: Support long string encryption
def rsa_decry(d_byte,key_in) :
    if len(d_byte) > 128 :
        out = ""
        for i in range(0,len(d_byte),128) :
            out = out + rsa.decrypt(d_byte[i:i+128], key_in).decode('utf8')
        return out
    else :
        result = rsa.decrypt(d_byte,key_in)
        return result.decode('utf8')

#PublicKey(n, e),
#PrivateKey(n, e, d, p, q)
def encode_pubkey(key_in) :
    return bytes(str(key_in.n) + "," + str(key_in.e),encoding='utf-8')

def encode_privkey(key_in) :
    return bytes(str(key_in.n) + "," + str(key_in.e) + "," + str(key_in.d) + "," + str(key_in.p) + "," + str(key_in.q),encoding='utf-8')

#generate public key by std str:
def gen_pubkey(str_pubkey) :
    key_li =  [int(v) for v in str_pubkey.split(',')]
    return rsa.PublicKey(key_li[0],key_li[1])

#generate private key by std str:
def gen_privkey(str_privkey) :
    key_li =  [int(v) for v in str_privkey.split(',')]
    return rsa.PrivateKey(key_li[0],key_li[1],key_li[2],key_li[3],key_li[4])

def savekey2file(key,file_name) :
    numlist = key.split(',')
    file = open(file_name,"w")
    file.write('\n'.join(numlist))
    file.close()

def readkeybyfile(file_name) :
    file = open(file_name,"r")
    KeyContent = file.read().split('\n')
    if len(KeyContent) == 2 :
        return gen_pubkey(','.join(KeyContent))
    else :
        return gen_privkey(','.join(KeyContent))

