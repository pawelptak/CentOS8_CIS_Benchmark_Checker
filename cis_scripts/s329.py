import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.2.9 Ensure IPv6 router advertisements are not accepted: "
    print(printed,end='')
    a= False
    output = os.popen('sysctl net.ipv6.conf.all.accept_ra').read()
    if('net.ipv6.conf.all.accept_ra = 0' in output):
        a=True

    b = False
    output = os.popen('sysctl net.ipv6.conf.default.accept_ra').read()
    if ('net.ipv6.conf.default.accept_ra = 0' in output):
        b = True

    c = False
    output = os.popen('grep "net\.ipv6\.conf\.all\.accept_ra" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv6.conf.all.accept_ra = 0' in output):
        c = True

    d = False
    output = os.popen('grep "net\.ipv6\.conf\.default\.accept_ra" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv6.conf.default.accept_ra = 0' in output):
        d = True

    if(a and b and c and d):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

