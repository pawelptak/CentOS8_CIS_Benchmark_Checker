import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.7.1.4 Ensure the SELinux state is enforcing: "
    print(printed,end='')
    one= False
    searched=r"'^\s*SELINUX=enforcing'"
    output = os.popen('grep -E '+searched+' /etc/selinux/config').read()
    if("SELINUX=enforcing" in output):
        one=True
    two=False
    output = os.popen('sestatus').read()
    if ("Current mode:                   enforcing" in output and "Mode from config file:          enforcing" in output):
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

