import os
import linecache

temps = open("admin_users.txt","w")
file = "users.txt"
ln = 180

while ln < 221:
    line = linecache.getline(file, ln).strip()
    temps.write(line + '\n')
    os.system("usermod -a -G temp " + line)
    ln +=1

temps.close()

