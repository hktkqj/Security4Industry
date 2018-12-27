import socket
import os
import time
import rsa
import RSAbase

config = {}
devices = {}
pubkey, privkey = rsa.newkeys(1024)

#启动时从DNC.cfg中导入配置，包括ip/MAC/port
#同时从Devices.cfg中导入设备信息，包括各设备的端口号和ip
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

#用于记录保存日志信息
def Log(msg) :
    LogFile = open("Record.log","a")
    msg = time.asctime( time.localtime(time.time()) ) + " | " + msg + '\n'
    LogFile.write(msg)
    LogFile.close()

#响应询问状态信息
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
                stasock.sendall(bytes("end", encoding="utf-8"))
                stasock.close()
            except :
                ret = "Unreachable"
            SendBack.append("Device %d status :%s" % (dev[0],ret))
    else :
        Log("Request status of device " + ",".join(Device))
        for num1 in Device :
            num = int(num1)
            stasock = socket.socket()
            try:
                stasock.connect(devices[num])
                stasock.sendall(bytes("request", encoding="utf-8"))
                ret = str(stasock.recv(1024), encoding="utf-8")
                print(ret)
                stasock.sendall(bytes("end", encoding="utf-8"))
                stasock.close()
            except:
                ret = "Unreachable"
            SendBack.append("Device %d status :%s" % (num, ret))
    return '\n'.join(SendBack)

#响应部署信息
def RequestDeploy(Command) :
    Data = Command.split("~~~")
    Device = Data[0].split("|||")
    Content = Data[1]
    SendBack = []
    if Device[0] == "A" :
        Message = "Deploy file to all device. File="
        for dev in devices.items() :
            stasock = socket.socket()
            try :
                stasock.connect(dev[1])
                stasock.sendall(bytes(Content,encoding="utf-8"))
                ret = str(stasock.recv(1024), encoding="utf-8")
                stasock.sendall(bytes("end", encoding="utf-8"))
                stasock.close()
            except :
                ret = "Unreachable"
            SendBack.append("Device %d  :%s" % (dev[0],ret))
    else :
        Message = "Deploy file to device " + ",".join(Device) + ". File="
        for num1 in Device :
            num = int(num1)
            stasock = socket.socket()
            try:
                stasock.connect(devices[num])
                stasock.sendall(bytes(Content, encoding="utf-8"))
                ret = str(stasock.recv(1024), encoding="utf-8")
                stasock.sendall(bytes("end", encoding="utf-8"))
                stasock.close()
            except:
                ret = "Unreachable"
            SendBack.append("Device %d status :%s" % (num, ret))
    DeployLogFileName = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()) + ".dpl"
    DeployLogFile = open(DeployLogFileName,"w")
    DeployLogFile.write(Content)
    DeployLogFile.close()
    AbsPath = os.getcwd() + "\\" + DeployLogFileName
    Log(Message + '"%s"' % AbsPath)
    return '\n'.join(SendBack)

#用来将密钥文件下发至NC设备
def sendMESPubkey2NC(byte_key) :
    retli = []
    byte_key = bytes("key:" + str(byte_key,encoding='utf-8') , encoding='utf-8')
    for dev in devices.items():
        stasock = socket.socket()
        try:
            stasock.connect(dev[1])
            stasock.send(byte_key)
            ret = str(stasock.recv(1024), encoding="utf-8")
            retli.append("(%s,%s)-%s"%(dev[1][0],str(dev[1][1]),ret))
            stasock.send(bytes("end",encoding='utf-8'))
            stasock.close()
        except:
            pass
    return retli

#主服务程序，用来接收MES发送来的信息
def StartService():
    #端口绑定
    sk = socket.socket()
    sk.bind((config["host"],int(config["port"])))
    sk.listen(1)
    while True :
        client, addr = sk.accept()
        #记录登陆信息
        Log("Log in from %s" % addr[0])
        #每次连接后更新MES公钥文件
        ret_bytes = client.recv(102400)
        RSAbase.savekey2file(str(ret_bytes,encoding="utf-8"),"MES.key")
        #同时将接收到的密钥下发到NC设备
        client.send(bytes('&'.join(sendMESPubkey2NC(ret_bytes)),encoding='utf-8'))
        while True :
            ret_bytes = client.recv(102400)
            Receive = str(ret_bytes,encoding="utf-8")
            #根据MES的不同请求来控制NC设备
            if (Receive == "finish") :
                break
            if (Receive.split(" ")[0] == "status") :
                client.send(bytes(RequestStatus(Receive.split(" ")),encoding='utf-8'))
            if (Receive.split(" ")[0] == "deploy") :
                client.send(bytes(RequestDeploy(Receive.split(" ")[1]),encoding='utf-8'))
        client.close()
        Log("Log out from %s" % addr[0])
    sk.close()

if __name__ == '__main__':
    #导入配置
    configinport()
    #开始服务
    StartService()



