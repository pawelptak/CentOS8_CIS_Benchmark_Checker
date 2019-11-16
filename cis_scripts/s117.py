import os
import termcolor

def check():
    results=[]
    printed="1.1.7 Ensure separate partition exists for /var/tmp: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep /var/tmp").read()
    if("on /var/tmp type xfs (rw,nosuid,nodev,noexec,relatime)" in output):
        one=True

    if(one):
        printed+="Success"
        results.append("1")
        print(termcolor.colored('Success', 'green'))
    else:
        printed += "Failed"
        results.append("0")
        print(termcolor.colored('Failed', 'red'))
    results.append(printed)
    return results

