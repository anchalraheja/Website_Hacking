import os
import commands
import subprocess
import re 
f = open("server.txt")
for user in f.readlines():
	out = subprocess.check_output("ping -n 1 " + user, shell=True )
	regex = r"(\d+)(.)(\d+)(.)(\d+)(.)(\d+)"
	x = re.search(regex, out)
	print x.group(0) + "  " + user
