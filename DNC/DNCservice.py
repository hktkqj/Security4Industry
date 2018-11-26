import socket
import os
import time
config = {}
devices = {}

def configinport():
    cfgfile = open("DNC.cfg")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    for i in range(0,4) :
        config[content[i].split(' ')[0]] = content[i].split(' ')[2]
    cfgfile = open("Devices.cfg","r")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    while '' in content :
        content.remove('')
    for dev in content :
        detail = dev.split(',')
        devices[int(detail[0])] = (detail[1].split('=')[1],int(detail[2].split('=')[1]))

def Log(msg) :
    LogFile = open("Record.log","a")
    msg = time.asctime( time.localtime(time.time()) ) + " | " + msg + '\n'
    LogFile.write(msg)
    LogFile.close()

def RequestStatus(Command) :
    if "A" in Command :
        Device = ["A"]
    else :
        Device = Command[1:]
    SendBack = []
    if (Device[0]=="A") :
        Log("Request all devices status")
        for dev in devices.items() :
            stasock = socket.socket()
            try :
                stasock.connect(dev[1])
                stasock.sendall(bytes("request",encoding="utf-8"))
                ret = str(stasock.recv(1024), encoding="utf-8")
                stasock.close()
            except :
                ret = "Unreachable"
            SendBack.append("Device %d status :%s" % (dev[0],ret))
    else :
        Log("Request status of device " + ",".join(Device))
        for num1 in Device :
            num = int(num1)
            print(devices[num])
            stasock = socket.socket()
            try:
                stasock.connect(devices[num])
                stasock.sendall(bytes("request", encoding="utf-8"))
                ret = str(stasock.recv(1024), encoding="utf-8")
                stasock.close()
            except:
                ret = "Unreachable"
            print("Device %d status :%s" % (num, ret))

def RequestDeploy(Command) :
    Data = Command.split("~~~")
    Device = Data[0].split("|||")
    Content = Data[1]
    if Device[0] == "A" :
        Message = "Deploy file to all device. File="
    else :
        Message = "Deploy file to device " + ",".join(Device) + ". File="
    DeployLogFileName = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()) + ".dpl"
    DeployLogFile = open(DeployLogFileName,"w")
    DeployLogFile.write(Content)
    DeployLogFile.close()
    AbsPath = os.getcwd() + "\\" + DeployLogFileName
    Log(Message + '"%s"' % AbsPath)


def StartService():
    sk = socket.socket()
    sk.bind((config["host"],int(config["port"])))
    sk.listen(1)
    while True :
        client, addr = sk.accept()
        Log("Log in from %s" % addr[0])
        while True :
            ret_bytes = client.recv(10240)
            Receive = str(ret_bytes,encoding="utf-8")
            if (Receive == "finish") :
                break
            if (Receive.split(" ")[0] == "status") :
                RequestStatus(Receive.split(" "))
            if (Receive.split(" ")[0] == "deploy") :
                RequestDeploy(Receive.split(" ")[1])
        client.close()
        Log("Log out from %s" % addr[0])
    sk.close()

if __name__ == '__main__':
    configinport()
    StartService()



