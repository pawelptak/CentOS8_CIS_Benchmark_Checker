import os
import termcolor

def check():
    results=[]
    printed="1.1.1.3 Ensure mounting of squashfs filesystems is disabled: "
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
        print(termcolor.colored('Success', 'green'))
    else:
        printed += "Failed"
        results.append("0")
        print(termcolor.colored('Failed', 'red'))
    results.append(printed)
    return results

