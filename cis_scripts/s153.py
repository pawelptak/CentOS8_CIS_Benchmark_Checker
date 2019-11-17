import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.5.3 Ensure authentication required for single user mode: "
    print(printed,end='')
    one= False
    output = os.popen("grep /systemd-sulogin-shell /usr/lib/systemd/system/rescue.service").read()
    if("ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue" in output):
        one=True
    two=False
    output = os.popen("grep /systemd-sulogin-shell /usr/lib/systemd/system/emergency.service").read()
    if ("ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency" in output):
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

