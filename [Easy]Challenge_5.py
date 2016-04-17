#Your challenge for today is to create a program which is password protected,
#and wont open unless the correct user and password is given.
#For extra credit, have the user and password in a seperate .txt file.
#for even more extra credit, break into your own program :)

import getpass

u = raw_input("Username: ")
p = getpass.getpass()

uFile = open("user.txt", 'r')
rUser = uFile.readline()
uFile.close()

pFile = open('pass.txt', 'r')
rPass = pFile.readline()
pFile.close()

if u == rUser and p == rPass:
	print("Username and Password accepted. Welcome.")
else:
	print("Information incorrect.")