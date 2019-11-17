import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.7.1.2 Ensure SELinux is not disabled in bootloader configuration: "
    print(printed,end='')
    one= False
    searched=r"'kernelopts=(\S+\s+)*(selinux=0|enforcing=0)+\b'"
    output = os.popen('grep -E '+searched+' /boot/grub2/grubenv').read()
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

