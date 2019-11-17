import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.1.4 Ensure nosuid option set on /tmp partition: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep -E '\s/tmp\s' | grep -v nosuid").read()
    if(output==""):
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

