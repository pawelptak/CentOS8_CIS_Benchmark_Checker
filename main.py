import s1111
import s1112
import s1113
import s1114
import s112
import s113
import s114
import s115
import s116
import s117
import s118
import s119
import s11_10
import s11_11

file=open("report.txt","w+")
file.writelines("CIS Policy Check Results\n\n")

file.writelines("1.1.1 Disable unused filesystems \n\n")

results=s1111.check()
file.writelines(results[1]+"\n")

results=s1112.check()
file.writelines(results[1]+"\n")

results=s1113.check()
file.writelines(results[1]+"\n")

results=s1114.check()
file.writelines(results[1]+"\n")

results=s112.check()
file.writelines(results[1]+"\n")

results=s113.check()
file.writelines(results[1]+"\n")

results=s114.check()
file.writelines(results[1]+"\n")

results=s115.check()
file.writelines(results[1]+"\n")

results=s116.check()
file.writelines(results[1]+"\n")

results=s117.check()
file.writelines(results[1]+"\n")

results=s118.check()
file.writelines(results[1]+"\n")

results=s119.check()
file.writelines(results[1]+"\n")

results=s11_10.check()
file.writelines(results[1]+"\n")

results=s11_11.check()
file.writelines(results[1]+"\n")