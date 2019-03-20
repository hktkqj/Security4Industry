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

def generate_time_test_module() :
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


def Encry_decry_time_test():
    bit = 256
    while bit <= 2048:
        length = 10
        pubkey, privkey = rsa.newkeys(bit)
        while length <= 10000:
            test_str = generate_random_str(length)
            a = datetime.now()
            RSAbase.rsa_encry(test_str, pubkey, bit)
            b = datetime.now()
            encry_time = b - a
            print("Status : str_length = %d, key_bit = %d;" % (length, bit))
            print("\tEncry time: ", encry_time, ", Decry time: ", end="")
            temp = RSAbase.rsa_encry(test_str, pubkey, bit)
            a = datetime.now()
            RSAbase.rsa_decry(temp, privkey, bit)
            b = datetime.now()
            result = RSAbase.rsa_decry(temp, privkey, bit)
            decry_time = b - a
            print(decry_time)
            print("\tEncry_str=%s\n\tDecry_str=%s\n\tCompare: match" % (test_str, result))
            length *= 10
        bit *= 2

if __name__ == '__main__':
    pass
    # time_test_module()
    # Encry_decry_time_test()

