import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.8.1.5 Ensure permissions on /etc/issue are configured: "
    print(printed,end='')
    one= False
    output = os.popen('stat /etc/issue').read()
    if("0644" in output and "Uid: (    0/" in output and "Gid: (    0/" in output):
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

