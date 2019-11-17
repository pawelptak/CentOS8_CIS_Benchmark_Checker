import os


class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results = []
    printed = "\t1.6.1 Ensure core dumps are restricted: "
    print(printed, end='')
    one = False
    command=r'grep -E "^\s*\*\s+hard\s+core" /etc/security/limits.conf'
    output = os.popen(command).read()
    if ("* hard core 0" in output):
        one = True
    command=r'grep -E ""^\s*\*\s+hard\s+core"" /etc/security/limits.d/*'
    output = os.popen(command)
    if ("* hard core 0" in output):
        one = True
    two = False
    output = os.popen("sysctl fs.suid_dumpable").read()
    if ("fs.suid_dumpable = 0" in output):
        two = True
    three = False
    output = os.popen("grep ""fs\.suid_dumpable"" /etc/sysctl.conf /etc/sysctl.d/*").read()
    if ("fs.suid_dumpable = 0" in output):
        three = True
    if (one and two and three):
        printed += "Success"
        results.append("1")
        print(colors.SUCC + "Success" + colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL + "Failed" + colors.NONE)
    results.append(printed)
    return results
