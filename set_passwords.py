import os
logins = open("userspass.txt", "r")

for login in logins:
    uname = login.split()
    username = uname[0]
    password = uname[1]
    upass = open("pass.txt", "a")
    pw = username + ":" + password
    upass.write(pw + "\n")
    os.system("cat pass.txt |chpasswd")




