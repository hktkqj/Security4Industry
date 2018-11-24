import socket
import os
config = {}

def configinport():
    cfgfile = open("DNC.cfg")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    for i in range(0,4) :
        config[content[i].split(' ')[0]] = content[i].split(' ')[2]

def RequestStatus(Command,Client) :
    if "A" in Command :
        Device = ["A"]
    else :
        Device = Command[1:]
    print(Device)

def RequestDeploy(Command,Client) :
    Data = Command.split("~~~")
    Device = Data[0].split("|||")
    Content = Data[1]
    print(Device)
    print(Content)

def StartService():
    sk = socket.socket()
    sk.bind((config["host"],int(config["port"])))
    sk.listen(1)
    while True :
        client, addr = sk.accept()
        while True :
            ret_bytes = client.recv(10240)
            Receive = str(ret_bytes,encoding="utf-8")
            if (Receive == "finish") :
                break
            if (Receive.split(" ")[0] == "status") :
                RequestStatus(Receive.split(" "),client)
            if (Receive.split(" ")[0] == "deploy") :
                RequestDeploy(Receive.split(" ")[1],client)
        client.close()
        print("finished")
    sk.close()

if __name__ == '__main__':
    configinport()
    StartService()



