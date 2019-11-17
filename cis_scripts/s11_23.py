import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'

def check():
    results=[]
    printed="\t1.1.23 Disable USB Storage: "
    print(printed,end='')
    one= False
    output = os.popen("modprobe -n -v usb-storage").read()
    if("install /bin/true" in output):
        one=True
    two=False
    output=os.popen("lsmod | grep usb-storage").read()
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
        print(colors.SUCC+"Failed"+colors.NONE)
    results.append(printed)
    return results

