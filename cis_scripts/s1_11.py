import os
class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results=[]
    printed="\t1.11 Ensure system-wide crypto policy is FUTURE or FIPS: "
    print(printed,end='')
    one= False
    command=r"grep -E -i '^\s*(FUTURE|FIPS)\s*(\s+#.*)?$' /etc/crypto-policies/config"
    output = os.popen(command).read()
    if("FUTURE" in output or "FIPS" in output):
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

