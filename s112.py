import os
import termcolor

def check():
    results=[]
    printed="1.1.2 Ensure /tmp is configured: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep -E '\s/tmp\s'").read()
    if("tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime)" in output):
        one=True
    two=False
    output=os.popen("systemctl is-enabled tmp.mount").read()
    if(output=="enabled"):
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

