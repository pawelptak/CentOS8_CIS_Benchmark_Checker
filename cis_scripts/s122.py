import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.2.2 Ensure gpgcheck is globally activated: "
    print(printed,end='')
    one= False
    output = os.popen("grep ^gpgcheck /etc/yum.conf").read()
    if("gpgcheck=0" not in output):
        one=True
    two = False
    output = os.popen("grep ^gpgcheck /etc/yum.repos.d/*").read()
    if ("gpgcheck=0" not in output):
        two = True

    if(one and two):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results





















