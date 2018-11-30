import socket
import time
import os
import rsa
import RSAbase

config = {}
ConnectFlag = False
pubkey, privkey = rsa.newkeys(1024)

tryConnect = socket.socket()

def ConfigImport():
    cfgfile = open("MES.cfg")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    for i in range(0,4) :
        config[content[i].split(' ')[0]] = content[i].split(' ')[2]


def Connect2Server():
    try :
        tryConnect.connect((config['target'],int(config['port'])))
        print("Connect to server %s (port %s) successfully" % (config['target'],config['port']))
        tryConnect.send(RSAbase.encode_pubkey(pubkey))
        keys = str(tryConnect.recv(102400),encoding='utf-8').split('&')
        for key in keys:
            key = key.split('-')
            print(key)
            dev = key[0]
            RSAbase.savekey2file(key[1], dev+'.key')
        return True
    except :
        print("Unable reach server %s (port %s)" % (config['target'],config['port']))
        return False


def deploy(Command):
    if '"' in Command :
        Command = Command.split("\"")
        while '' in Command :
            Command.remove('')
        if len(Command) <= 2 :
            print("Improper argument number.")
            return
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
        Command = Command.split(' ')
        while '' in Command :
            Command.remove('')
        if len(Command) <= 2 :
            print("Improper argument number.")
            return
        if os.path.exists(Command[1]) :
            file = open(Command[1],"r")
            Content = file.read()
        else :
            print("No such file to deploy.")
            return
        device = Command[2:]
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
    if len(Content) >= 102400 :
        print("Deploy file too big.")
        return
    sendmsg = "deploy " + device + "~~~" + Content
    try:
        tryConnect.sendall(sendmsg.encode('utf-8'))
        return str(tryConnect.recv(102400),encoding='utf-8')
    except:
        print("You are now disconnected from server")
        return


def status(Command):
    while '' in Command :
        Command.remove('')
    if len(Command) == 1:
        print("Improper argument number.")
        return
    flag = True
    if 'A' in Command :
        sendmsg = "status A"
        try:
            tryConnect.sendall(sendmsg.encode('utf-8'))
        except:
            print("You are now disconnected from server")
            return
    else :
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
    return str(tryConnect.recv(10240),encoding="utf-8")

def FunctionCycle():
    function = ["status", "deploy", "help", "exit"]
    help = {"status":"Show status for NC device.\nUsage: status [device1] [device2] ... [A] [/?]",
            "deploy":"Deploy acsii commmand to NC device.\nUsage: deploy [acsii_file_path] [device1] [device2] ... [A] [/?]",
            "help"  :'Available command :"status", "deploy", "help", "exit";\nType "COMMAND /?" for details.'
            }
    print("MES contorl center")
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
    ConfigImport()
    if Connect2Server() == True :
        FunctionCycle()
    else :
        print("Program shutting down...")
        time.sleep(1.5)