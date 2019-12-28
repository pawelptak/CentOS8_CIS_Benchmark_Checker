import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.4.4.1.1 Ensure default deny firewall policy: "
    print(printed,end='')
    a=False
    output = os.popen('iptables -L').read()
    if('Chain INPUT (policy DROP)' in output or 'Chain INPUT (policy REJECT)' in output):
        if ('Chain FORWARD (policy DROP)' in output or 'Chain FORWARD (policy REJECT)' in output):
            if ('Chain OUTPUT (policy DROP)' in output or 'Chain OUTPUT (policy REJECT)' in output):
                a=True



    if(a):
        printed+="Success"
        results.append("1")
        print(colors.SUCC+"Success"+colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL+"Failed"+colors.NONE)
    results.append(printed)
    return results

