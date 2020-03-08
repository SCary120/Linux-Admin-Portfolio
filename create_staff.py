import os
import linecache

staff = open("staff_users.txt","w")
file = "users.txt"
ln = 81

while ln < 180:
    line = linecache.getline(file, ln).strip()
    staff.write(line + '\n')
    os.system("usermod -a -G staff " + line)
    ln +=1

staff.close()

