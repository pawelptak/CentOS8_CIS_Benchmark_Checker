import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.1.12 Ensure separate partition exists for /var/log/audit: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep /var/log/audit").read()
    if("/dev/xvdi1 on /var/log/audit type xfs (rw,relatime,data=ordered)" in output):
        one=True

    if(one):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

