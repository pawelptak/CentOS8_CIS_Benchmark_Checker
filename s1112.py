import os
import termcolor

def check():
    results=[]
    printed="1.1.1.2 Ensure mounting of vFAT filesystems is limited: "
    print(printed,end='')
    one= False
    output = os.popen("modprobe -n -v vfat").read()
    if("install /bin/true" in output):
        one=True
    two=False
    output=os.popen("lsmod | grep vfat").read()
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

