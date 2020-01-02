import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t3.4.4.1.4 Ensure firewall rules exist for all open ports: "
    print(printed,end='')
    a=True
    output = os.popen("ss -4tuln | grep LISTEN | grep -v 127.0.0.1 | awk '{print $1,$5}'").read()
    if (output!=''):
        for line in output.split('\n'):
            protocol='none'
            if('tcp' in line):
                protocol='tcp'
            else:
                protocol='udp'
            i=line.find(':')
            portNumber=line[i+1:]
            if(portNumber!=''):
                searchPhrase='-A INPUT -p '+protocol+' -m '+protocol+' --dport '+portNumber+' -m state --state NEW -j ACCEPT'
                check= os.popen('iptables-save | grep -- "'+searchPhrase+'"').read()
                if (check == ''):
                    a=False
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
