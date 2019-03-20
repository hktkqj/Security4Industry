import rsa
import random
import string

def generate_random_str(len) :
    set = string.ascii_letters
    str = []
    for i in range(0,len) :
        str.append(random.choice(set))
    return ''.join(str)


pubkey, pirvkey = rsa.newkeys(1024)
anopubkey, anoprivkey = rsa.newkeys(1024)
strs = generate_random_str(10000)

signature = rsa.sign(strs.encode('utf8'),priv_key=pirvkey,hash_method='SHA-256')
print(len(signature))
signature1 = rsa.sign(strs.encode('utf8'),priv_key=anoprivkey,hash_method='SHA-256')

rsa.verify(strs.encode('utf8'),signature=signature,pub_key=pubkey)
