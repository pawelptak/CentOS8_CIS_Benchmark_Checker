import sys
from cis_scripts import *

sum=0
passed=0
file=open("report.txt","w+")
file.writelines("CIS Policy Check Results\n")



def execute(script):
    results=script.check()
    file.writelines(results[1]+"\n")
    if(results[0]=="1"):
        return 1
    else:
        return 0

file.writelines("\n1.1.1 Disable unused filesystems\n")
passed+=execute(s1111)
sum+=1
passed+=execute(s1112)
sum+=1
passed+=execute(s1113)
sum+=1
passed+=execute(s1114)
sum+=1
passed+=execute(s112)
sum+=1
passed+=execute(s113)
sum+=1
passed+=execute(s114)
sum+=1
passed+=execute(s115)
sum+=1
passed+=execute(s116)
sum+=1
passed+=execute(s117)
sum+=1
passed+=execute(s118)
sum+=1
passed+=execute(s119)
sum+=1
passed+=execute(s11_10)
sum+=1
passed+=execute(s11_11)
sum+=1
passed+=execute(s11_12)
sum+=1
passed+=execute(s11_13)
sum+=1
passed+=execute(s11_14)
sum+=1
passed+=execute(s11_15)
sum+=1
passed+=execute(s11_16)
sum+=1
passed+=execute(s11_17)
sum+=1
passed+=execute(s11_21)
sum+=1
passed+=execute(s11_22)
sum+=1
passed+=execute(s11_23)
sum+=1

file.writelines("\n1.2 Configure Software Updates\n")
passed+=execute(s122)
sum+=1

file.writelines("\n1.3 Configure sudo\n")
passed+=execute(s131)
sum+=1
passed+=execute(s132)
sum+=1
passed+=execute(s133)
sum+=1

file.writelines("\n1.4 Filesystem Integrity Checking\n")
passed+=execute(s141)
sum+=1

file.writelines("\n1.5 Secure Boot Settings\n")
passed+=execute(s151)
sum+=1
passed+=execute(s152)
sum+=1
passed+=execute(s153)
sum+=1

file.writelines("\n1.6 Additional Process Hardening\n")
passed+=execute(s161)
sum+=1
passed+=execute(s162)
sum+=1

file.writelines("\n1.7.1 Configure SELinux\n")
passed+=execute(s1711)
sum+=1
passed+=execute(s1712)
sum+=1
passed+=execute(s1713)
sum+=1
passed+=execute(s1714)
sum+=1
passed+=execute(s1715)
sum+=1
passed+=execute(s1716)
sum+=1
passed+=execute(s1717)
sum+=1

file.writelines("\n1.8.1 Command Line Warning Banners\n")
passed+=execute(s1814)
sum+=1
passed+=execute(s1815)
sum+=1
passed+=execute(s1816)
sum+=1
passed+=execute(s1_10)
sum+=1
passed+=execute(s1_11)
sum+=1

file.writelines("\n2.1 inetd Services\n")
passed+=execute(s211)
sum+=1

file.writelines("\n2.2.1 Time Synchronization\n")
passed+=execute(s2211)
sum+=1
passed+=execute(s2212)
sum+=1

file.writelines("\n3.1 Network Parameters (Host Only)\n")
passed+=execute(s311)
sum+=1
passed+=execute(s312)
sum+=1

file.writelines("\n3.2 Network Parameters (Host and Router)\n")
passed+=execute(s321)
sum+=1
passed+=execute(s322)
sum+=1
passed+=execute(s323)
sum+=1
passed+=execute(s324)
sum+=1
passed+=execute(s325)
sum+=1
passed+=execute(s326)
sum+=1
passed+=execute(s327)
sum+=1
passed+=execute(s329)
sum+=1

file.writelines("\n3.4.4 Configure iptables\n")
passed+=execute(s34411)
sum+=1

file.writelines("\nPassed: "+str(passed)+"/"+str(sum)+" ("+str(round(float(passed/sum*100),2))+"%)")

