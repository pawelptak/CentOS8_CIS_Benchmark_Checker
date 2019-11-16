import os
import termcolor

def check():
    results=[]
    printed="1.1.6 Ensure separate partition exists for /var: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep -E '\s/var\s'").read()
    if("/dev/xvdg1 on /var type xfs (rw,relatime,data=ordered)" in output):
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

