import socket
import time
import os
import rsa
import RSAbase

config = {}
ConnectFlag = False
pubkey, privkey = rsa.newkeys(1024)

tryConnect = socket.socket()
#导入MES配置文件
def ConfigImport():
    cfgfile = open("MES.cfg")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    for i in range(0,4) :
        config[content[i].split(' ')[0]] = content[i].split(' ')[2]

#尝试连接到服务器
def Connect2Server():
    try :
        tryConnect.connect((config['target'],int(config['port'])))
        print("Connect to server %s (port %s) successfully" % (config['target'],config['port']))
        tryConnect.send(RSAbase.encode_pubkey(pubkey))
        keys = str(tryConnect.recv(102400),encoding='utf-8').split('&')
        for key in keys:
            key = key.split('-')
            dev = key[0]
            RSAbase.savekey2file(key[1], dev+'.key')
        return True
    except :
        print("Unable reach server %s (port %s)" % (config['target'],config['port']))
        return False

#处理部署命令
def deploy(Command):
    if '"' in Command :
        #若使用双引号文件名路径
        Command = Command.split("\"")
        while '' in Command :
            Command.remove('')
        #判断参数是否合法
        if len(Command) <= 2 :
            print("Improper argument number.")
            return
        #判断文件是否存在
        if os.path.exists(Command[1]) :
            file = open(Command[1],"r")
            Content = file.read()
        else :
            print("No such file to deploy.")
            return
        device = Command[2].split(' ')
        while '' in device:
            device.remove('')
    else :
        #否则从当前目录下打开待部署文件
        Command = Command.split(' ')
        while '' in Command :
            Command.remove('')
        # 判断参数是否合法
        if len(Command) <= 2 :
            print("Improper argument number.")
            return
        # 判断文件是否存在
        if os.path.exists(Command[1]) :
            file = open(Command[1],"r")
            Content = file.read()
        else :
            print("No such file to deploy.")
            return
        device = Command[2:]
    #处理发送的设备
    if 'A' in device :
        device = "A"
    else :
        flag = True
        for dev in device :
            try :
                num = int(dev)
            except :
                flag=False
                break
        if flag == False :
            print("Illegal argument(s) in deploy command.")
            return
        else :
            device='|||'.join(device)
    #判断发送文件长度
    if len(Content) >= 102400 :
        print("Deploy file too big.")
        return
    sendmsg = "deploy " + device + "~~~" + Content
    try:
        #发送文件
        tryConnect.sendall(sendmsg.encode('utf-8'))
        return str(tryConnect.recv(102400),encoding='utf-8')
    except:
        print("You are now disconnected from server")
        return

#对status命令处理部分
def status(Command):
    #清除多余空格
    while '' in Command :
        Command.remove('')
    #判断参数是否合法
    if len(Command) == 1:
        print("Improper argument number.")
        return
    flag = True
    #如果包含'A'参数
    if 'A' in Command :
        sendmsg = "status A"
        try:
            tryConnect.sendall(sendmsg.encode('utf-8'))
        except:
            print("You are now disconnected from server")
            return
    else :
        #枚举所有设备 向其发送询问信息
        for i in range(1,len(Command)) :
            try :
                num = int(Command[i])
            except :
                flag = False
                break
        if flag == False :
            print("Illegal argument(s) in status command.")
            return
        sendmsg = ""
        for item in Command :
            sendmsg = sendmsg + item  + " "
        try :
            tryConnect.sendall(sendmsg[0:-1].encode('utf-8'))
        except :
            print("You are now disconnected from server")
            return
    #接受返回信息
    return str(tryConnect.recv(10240),encoding="utf-8")

#提供了一个命令行界面
def FunctionCycle():
    '''
    包括了四种命令:status,deploy,help,exit
    status:用于查看设备状态，用法 status s [device1] [device2] ... [A(全部设备)] [/?]
    deploy:用于部署文件到NC设备 用法 deploy [file_path(待部署文件名)] [device1] [device2] ... [A(全部设备)] [/?]
    help:查看帮助信息
    exit:退出
    '''
    function = ["status", "deploy", "help", "exit"]
    help = {"status":"Show status for NC device.\nUsage: status [device1] [device2] ... [A] [/?]",
            "deploy":"Deploy acsii commmand to NC device.\nUsage: deploy [acsii_file_path] [device1] [device2] ... [A] [/?]",
            "help"  :'Available command :"status", "deploy", "help", "exit";\nType "COMMAND /?" for details.'
            }
    print("MES contorl center")
    #开始接受命令
    while True :
        print()
        Command = input("Command(type 'help' for help)\\")
        if ' ' in Command :
            Command = Command.split(' ')
            if Command[0] not in function :
                print("Command \"%s\" not found, please try again." % Command[0])
                continue
            if Command[0] == "help" or Command[0] == "exit" :
                print("Command \"%s\" has no argument(s), please try again." % Command[0])
                continue
            if Command[1] == "/?" :
                print(help[Command[0]])
                continue
            if Command[0] == "deploy" :
                print(deploy(' '.join(Command)))
            elif Command[0] == "status" :
                print(status(Command))
        else :
            if Command not in function :
                print("Command \"%s\" not found, please try again." % Command)
                continue
            if Command == "exit" :
                tryConnect.sendall("finish".encode('utf-8'))
                break
            elif Command == "help" :
                print(help["help"])
                continue
            else :
                print("Command \"%s\" should have argument(s), please try again." % Command)

if __name__ == '__main__':
    #导入MES配置
    ConfigImport()
    #测试与DNC服务器的连接，若连接成功进入命令行界面
    if Connect2Server() == True :
        FunctionCycle()
    else :
        #若出现问题直接退出
        print("Program shutting down...")
        time.sleep(1.5)