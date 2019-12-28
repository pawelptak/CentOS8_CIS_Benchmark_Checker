import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.2.2 Ensure ICMP redirects are not accepted: "
    print(printed,end='')
    a= False
    output = os.popen('sysctl net.ipv4.conf.all.accept_redirects').read()
    if('net.ipv4.conf.all.accept_redirects = 0' in output):
        a=True

    b = False
    output = os.popen('sysctl net.ipv4.conf.default.accept_redirects').read()
    if ('net.ipv4.conf.default.accept_redirects = 0' in output):
        b = True

    c = False
    output = os.popen('grep "net\.ipv4\.conf\.all\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv4.conf.all.accept_redirects= 0' in output):
        c = True

    d = False
    output = os.popen('grep "net\.ipv4\.conf\.default\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv4.conf.default.accept_redirects= 0' in output):
        d = True

    e = False
    output = os.popen('sysctl net.ipv6.conf.all.accept_redirects').read()
    if ('net.ipv6.conf.all.accept_redirects = 0' in output):
        e = True

    f = False
    output = os.popen('sysctl net.ipv6.conf.default.accept_redirects').read()
    if ('net.ipv6.conf.default.accept_redirects = 0' in output):
        f = True

    g = False
    output = os.popen('grep "net\.ipv6\.conf\.all\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv6.conf.all.accept_redirects= 0' in output):
        g = True

    h = False
    output = os.popen('grep "net\.ipv6\.conf\.default\.accept_redirects" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv6.conf.default.accept_redirects= 0' in output):
        h = True

    if(a and b and c and d and e and f and g and h):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

