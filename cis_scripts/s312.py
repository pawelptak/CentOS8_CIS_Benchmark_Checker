import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.1.2 Ensure packet redirect sending is disabled: "
    print(printed,end='')
    a= False
    output = os.popen('sysctl net.ipv4.conf.all.send_redirects').read()
    if('net.ipv4.conf.all.send_redirects = 0' in output):
        a=True

    b = False
    output = os.popen('sysctl net.ipv4.conf.default.send_redirects').read()
    if ('net.ipv4.conf.default.send_redirects = 0' in output):
        b = True

    c = False
    output = os.popen('grep "net\.ipv4\.conf\.all\.send_redirects" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv4.conf.all.send_redirects = 0' in output):
        c = True

    d = False
    output = os.popen('grep "net\.ipv4\.conf\.default\.send_redirects" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ('net.ipv4.conf.default.send_redirects= 0' in output):
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

