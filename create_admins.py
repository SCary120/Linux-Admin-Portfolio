import os
import linecache

admin = open("admin_users.txt","w")
file = "users.txt"
ln = 1

while ln < 21:
    line = linecache.getline(file, ln).strip()
    admin.write(line + '\n')
    os.system("usermod -a -G admin,wheel " + line)
    ln +=1

admin.close()


