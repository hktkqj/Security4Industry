config = {}

def configinport():
    cfgfile = open("DNC.cfg")
    content = cfgfile.read().split('\n')
    cfgfile.close()
    for i in range(0,4) :
        config[content[i].split(' ')[0]] = content[i].split(' ')[2]
    return config


def configoutput():

    while True :
        for item in config:
            print(item + "=" + config[item])
        keyv = input("Enter key to change(exit to save):")
        if keyv == "exit" :
            return
        if keyv in config :
            valv = input("Enter value:")
            config[keyv] = valv
        else :
            print("Invalid input!")


def write2config():
    cfgfile =  open('DNC.cfg','w')
    for item in config :
        cfgfile.write(item + " = " + config[item] + '\n')
    cfgfile.close()
    print("Config save successfully.")



if __name__ == '__main__':
    configinport()
    configoutput()
    write2config()
