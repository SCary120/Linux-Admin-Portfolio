import os
import linecache

devs = open("dev_users.txt","w")
file = "users.txt"
ln = 21

while ln < 81:
    line = linecache.getline(file, ln).strip()
    devs.write(line + '\n')
    os.system("usermod -a -G developers -s /bin/csh " + line)
    ln +=1

devs.close()

