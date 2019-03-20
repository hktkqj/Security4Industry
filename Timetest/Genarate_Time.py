import rsa
import socket
from datetime import datetime

def get_generate_time(bits) :
    a = datetime.now()
    pubkey, privkey = rsa.newkeys(bits)
    b=datetime.now()
    return b-a

bit = 64
while bit <= 4096 :
    time = get_generate_time(bit)
    print("Generate bit(s): %d, Generate time: " % (bit), end="")
    print(time)
    bit *= 2