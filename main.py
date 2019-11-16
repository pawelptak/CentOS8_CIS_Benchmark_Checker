import os
from os.path import dirname, basename, isfile, join
import glob
import io
from cis_scripts import *



sum=0
passed=0
file=open("report.txt","w+")
file.writelines("CIS Policy Check Results\n\n")

file.writelines("1.1.1 Disable unused filesystems \n\n")

def execute(script):
    results=script.check()
    file.writelines(results[1]+"\n")
    if(results[0]=="1"):
        return 1
    else:
        return 0


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

file.writelines("\nPassed: "+str(passed)+"/"+str(sum)+" ("+str(float(passed/sum*100))+"%)")

