import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.5.2 Ensure bootloader password is set: "
    print(printed,end='')
    one= False
    output = os.popen("grep ""^\s*GRUB2_PASSWORD"" /boot/grub2/user.cfg").read()
    if("GRUB2_PASSWORD=" in output):
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

