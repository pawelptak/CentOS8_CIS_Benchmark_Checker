import os


class colors:
    SUCC = '\033[92m'
    FAIL = '\033[91m'
    NONE = '\033[0m'


def check():
    results = []
    printed = "\t1.6.2 Ensure address space layout randomization (ASLR) is enabled: "
    print(printed, end='')
    one = False
    output = os.popen(r'sysctl kernel.randomize_va_space').read()
    if ("kernel.randomize_va_space = 2" in output):
        one = True
    two = False
    output = os.popen(r'grep "kernel\.randomize_va_space" /etc/sysctl.conf /etc/sysctl.d/*').read()
    if ("kernel.randomize_va_space = 2" in output):
        two = True
    if (one and two):
        printed += "Success"
        results.append("1")
        print(colors.SUCC + "Success" + colors.NONE)
    else:
        printed += "Failed"
        results.append("0")
        print(colors.FAIL + "Failed" + colors.NONE)
    results.append(printed)
    return results
