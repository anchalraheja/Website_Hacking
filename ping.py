import os
import commands

f = open("server.txt")
for user in f.readlines():
	os.system("ping -n 1 " + user)
