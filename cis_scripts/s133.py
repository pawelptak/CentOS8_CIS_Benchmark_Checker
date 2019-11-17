import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.3.3 Ensure sudo log file exists: "
    print(printed,end='')
    one= False
    output = os.popen("grep -Ei '^\s*Defaults\s+([^#]+,\s*)?logfile=' /etc/sudoers").read()
    if("Defaults logfile=""/var/log/sudo.log""" in output):
        one=True
    two=False
    output=os.popen("grep -Ei '^\s*Defaults\s+([^#]+,\s*)?logfile=' /etc/sudoers.d/*").read()
    if ("Defaults logfile=""/var/log/sudo.log""" in output):
        two = True
    if(one or two):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL + "Failed" + colors.NONE)
    results.append(printed)
    return results

