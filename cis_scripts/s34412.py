import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.4.4.1.2 Ensure loopback traffic is configured: "
    print(printed,end='')
    a=False
    output = os.popen('iptables-save | grep -- "-A INPUT -i lo -j ACCEPT"').read()
    if(output!=''):
        a=True

    b=False
    output = os.popen('iptables-save | grep -- "-A OUTPUT -o lo -j ACCEPT"').read()
    if (output != ''):
        b = True

    c = False
    output = os.popen('iptables-save | grep -- "-A INPUT -s 127.0.0.0/8 -j DROP"').read()
    if (output != ''):
        c = True
    if(a and b and c):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

