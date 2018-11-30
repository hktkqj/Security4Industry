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
    sock = socket.socket()
    sock.bind((config["host"],int(config["port"])))
    sock.listen(1)
    while True :
        client, addr = sock.accept()
        while True :
            ret_bytes = client.recv(102400)
            Receive = str(ret_bytes,encoding="utf-8")
            if Receive == "request" :
                client.sendall(bytes(status(),encoding='utf-8'))
            elif Receive == "end" :
                client.close()
                break
            elif "~~~" in Receive and "|||" in Receive:
                SaveDeployFile(Receive)
                client.send(bytes("Deployed successfully",encoding='utf-8'))
            else :
                RSAbase.savekey2file(Receive, "MES.key")
                client.send(bytes("Key accepted", encoding='utf-8'))

if __name__ == '__main__':
    if firstrun() == False :
        CreateCfgFile()
    else :
        configinport()
    GoOnline()

