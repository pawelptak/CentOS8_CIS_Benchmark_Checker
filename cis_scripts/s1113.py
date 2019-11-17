import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.1.1.3 Ensure mounting of squashfs filesystems is disabled: "
    print(printed,end='')
    one= False
    output = os.popen("modprobe -n -v squashfs").read()
    if("install /bin/true" in output):
        one=True
    two=False
    output=os.popen("lsmod | grep squashfs").read()
    if(output==""):
        two=True

    result = one and two
    if(result):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

