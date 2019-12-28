import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.2.6 Ensure bogus ICMP responses are ignored: "
    print(printed,end='')
    a= False
    output = os.popen('sysctl net.ipv4.icmp_ignore_bogus_error_responses').read()
    if('net.ipv4.icmp_ignore_bogus_error_responses = 1' in output):
        a=True

    b = False
    output = os.popen('grep -E -s "^\s*net\.ipv4\.icmp_ignore_bogus_error_responses\s*=\s*0" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf').read()
    if (output == ''):
        b = True

    if(a and b):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

