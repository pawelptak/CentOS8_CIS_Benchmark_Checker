import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.5.1 Ensure permissions on bootloader config are configured: "
    print(printed,end='')
    one= False
    output = os.popen("stat /boot/grub2/grub.cfg").read()
    if("Uid: (    0/" in output and "Gid: (    0/" in output):
        one=True
    two=False
    output = os.popen("stat /boot/grub2/grubenv").read()
    if ("Uid: (    0/" in output and "Gid: (    0/" in output):
        two = True
    if(one and two):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

