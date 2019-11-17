import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.3.2 Ensure sudo commands use pty: "
    print(printed,end='')
    one= False
    output = os.popen("grep -Ei '^\s*Defaults\s+(\[^#]+,\s*)?use_pty' /etc/sudoers").read()
    if("Defaults use_pty" in output):
        one=True
    two=False
    output=os.popen("grep -Ei '^\s*Defaults\s+(\[^#]+,\s*)?use_pty' /etc/sudoers.d/*").read()
    if ("Defaults use_pty" in output):
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

