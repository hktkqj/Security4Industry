import rsa
import string
import RSAbase
import random
from datetime import datetime


def get_generate_time(bits,message) :
    pubkey, privkey = rsa.newkeys(bits)
    a = datetime.now()
    RSAbase.rsa_encry(message,pubkey)
    b = datetime.now()

    Encryed_byte = RSAbase.rsa_encry(message,pubkey)
    c = datetime.now()
    RSAbase.rsa_decry(Encryed_byte, privkey)
    d = datetime.now()

    return b-a, d-c


def generate_random_str(len) :
    set = string.ascii_letters
    str = []
    for i in range(0,len) :
        str.append(random.choice(set))
    return ''.join(str)

def time_test_module() :
    bit = 256
    while bit <= 2048 :
        len = 4
        while len <= 64 :
            try :
                encry_time, decry_time = get_generate_time(bit,generate_random_str(len))
                print("Status: len = %d, key_bit = %d; " % (len, bit), end='')
                print("Encry_time = ",end='')
                print(encry_time, end=', Decry_time = ')
                print(decry_time)
            except :
                print("Status: len = %d, key_bit = %d; " % (len, bit), end='ERROR: Unavailable\n')
            finally :
                len *= 4
        bit *= 2

if __name__ == '__main__':
    # time_test_module()
    pubkey, privkey = rsa.newkeys(1024)
    test_str = generate_random_str(1000)
    print(test_str)
    result = RSAbase.rsa_encry(test_str,pubkey)
    print(RSAbase.rsa_decry(result,privkey))
    '''
    for i in range(1,1000) :
        try :
            RSAbase.rsa_encry(generate_random_str(i), pubkey)
            print("Success at %d" % i)
        except :
            print("Failed at %d" % i)
    '''