import os
import termcolor

def check():
    results=[]
    printed="1.1.8 Ensure nodev option set on /var/tmp partition: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep -E '\s/var/tmp\s' | grep -v nodev").read()
    if(output==""):
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

