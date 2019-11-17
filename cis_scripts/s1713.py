import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.7.1.3 Ensure SELinux policy is configured: "
    print(printed,end='')
    one= False
    searched=r"'^\s*SELINUXTYPE=(targeted|mls)\b'"
    output = os.popen('grep -E '+searched+' /etc/selinux/config').read()
    if("SELINUXTYPE=targeted" in output or "SELINUXTYPE=mls" in output):
        one=True
    two=False
    output = os.popen('sestatus | grep Loaded').read()
    if ("targeted" in output or "mls" in output):
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

