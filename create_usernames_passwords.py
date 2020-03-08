user = open("UserNamesLvl1.txt","r")
user1 = open("UserNamesLvl2.txt","r")
users = open("users.txt","w")

#Import random for numbers
from random import *
#Import lincache to parse text files
import linecache
#import time to pause actions
import time
#import os to execute OS commands.
import os
import re


# function to create users
def create_username():
    # for each line in file users, do the following
    for line in user:
        x = randint(10,99) # generate a two digit random number
        first = line[:1] # variable to take first character of line
        last = line.split() # split each word in the line into a list
        last1 = last[1] # variable for last name
        username = first + last1 + str(x) # combine variables to create user
        users.write(username + '\n') # write each combined variable to username file on a new line.
# code behaves same way below as it does above, this time reading Lvl2 username file.
    for line in user1:
        x = randint(10,100)
        first = line[:1]
        last = line.split()
        last1 = last[1]
        username = first + last1 + str(x)
        users.write(username + '\n')

# call function to create users
create_username()
# close text file
users.close()
# pause actions for 2 seconds
time.sleep(2)

# function to generate user passwords.
def gen_pass():
    passwd = open("userspass.txt", "w")
    users = "users.txt"
    ln = 1
    while ln < 221:
        # grab each line and strip white space
        line = linecache.getline(users, ln).strip()
        # generate 4 digit random numbers
        x = randint(1000,2000)
        # combine username and random 4 digits that will be used for password
        password = line + str(x)
        # write usernames and passwords to text file.
        passwd.write(line + " " + password + '\n')
        ln += 1
#call function
gen_pass()
# pause actions for 1 second
time.sleep(1)

logins = open("userspass.txt", "r")
# for loop that will create a user for each username generated in scripts above.
for login in logins:
    uname = login.split()
    username = uname[0]
    os.system("useradd -m " + username)







# incorporating Reg Ex.

#f = user.read()
#first = re.findall('.+', f)
#for item in first:
#    n = randint(10,100)
#    name = item.split()
#    fn = name[0]
#    last = name[1]
#    x = re.findall('[A-Z]', fn)
#    full = "".join(str(fn[0]) + str(last) + str(n))
#    print(full)

