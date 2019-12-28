import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.1.1 Ensure IP forwarding is disabled: "
    print(printed,end='')
    one= False
    output = os.popen('sysctl net.ipv4.ip_forward').read()
    if('net.ipv4.ip_forward = 0' in output):
        one=True

    two = False
    output = os.popen('grep -E -s "^\s*net\.ipv4\.ip_forward\s*=\s*1" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf').read()
    if (output==""):
        two = True

    three = False
    output = os.popen('sysctl net.ipv6.conf.all.forwarding').read()
    if ('net.ipv6.conf.all.forwarding' in output):
        three = True

    four = False
    output = os.popen('grep -E -s "^\s*net\.ipv6\.conf\.all\.forwarding\s*=\s*1" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf').read()
    if (output==""):
        four = True

    if(one and two and three and four):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

