import socket
import os
import uuid
import random
import time
import rsa
import RSAbase


pubkey, privkey = rsa.newkeys(1024)


def firstrun() :
    return os.path.exists("LocalConfig.cfg")


def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


def get_host_ip():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr


def CreateCfgFile() :
    CfgFile = open("LocalConfig.cfg","w")
    CfgFile.write("host = " + str(get_host_ip()) + "\n")
    CfgFile.write("MAC = " + str(get_mac_address()) + "\n")
    while True :
        port = input("Bind listening port:")
        try :
            port = int(port)
            break
        except :
            print("Invalid port.")
    CfgFile.write("port = " + str(port))
    CfgFile.close()


config = {}
def configinport():
    cfgfile = open("LocalConfig.cfg","r")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    for i in range(0,3) :
        config[content[i].split(' ')[0]] = content[i].split(' ')[2]


def status() :
    return random.choice(["Stand by","Working","Out of Order"])


def SaveDeployFile(data) :
    DeployLogFileName = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()) + ".dpl"
    DeployLogFile = open(DeployLogFileName, "w")
    DeployLogFile.write(data)
    DeployLogFile.close()


def GoOnline() :
    print("Device online, ip=%s, port=%s" % (config['host'],config['port']))
    Pubkey_recved = False
    sock = socket.socket()
    sock.bind((config["host"],int(config["port"])))
    sock.listen(1)
    while True :
        client, addr = sock.accept()
        while True :
            ret_bytes = client.recv(10240)
            if Pubkey_recved == False:
                Receive = str(ret_bytes,encoding='utf-8')
                RSAbase.savekey2file(Receive, "DNC.key")
                client.sendall(RSAbase.encode_pubkey(pubkey))
                Pubkey_recved = True
            else :
                try :
                    Receive = RSAbase.rsa_decry(ret_bytes, privkey)
                except :
                    continue
                if Receive == "request":
                    client.sendall(RSAbase.rsa_encry(status(), RSAbase.readkeybyfile("DNC.key")))
                elif Receive == "end":
                    client.close()
                    break
                else:
                    SaveDeployFile(Receive)
                    client.sendall(RSAbase.rsa_encry("Deployed successfully", RSAbase.readkeybyfile("DNC.key")))


if __name__ == '__main__':
    if firstrun() == False:
        CreateCfgFile()
    else :
        configinport()
    GoOnline()

