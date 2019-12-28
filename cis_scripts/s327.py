import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.2.7 Ensure Reverse Path Filtering is enabled: "
    print(printed,end='')
    a= False
    output = os.popen('sysctl net.ipv4.conf.all.rp_filter').read()
    if('net.ipv4.conf.all.rp_filter = 1' in output):
        a=True

    b = False
    output = os.popen('sysctl net.ipv4.conf.default.rp_filter').read()
    if ('net.ipv4.conf.default.rp_filter = 1' in output):
        b = True

    c = False
    output = os.popen('grep -E -s "^\s*net\.ipv4\.conf\.all\.rp_filter\s*=\s*0" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf').read()
    if (output == ''):
        c = True

    d = False
    output = os.popen('grep -E -s "^\s*net\.ipv4\.conf\.default\.rp_filter\s*=\s*1" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf').read()
    if ('net.ipv4.conf.default.rp_filter = 1' in output):
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

