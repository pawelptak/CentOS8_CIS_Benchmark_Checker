import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.1.2 Ensure /tmp is configured: "
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
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

