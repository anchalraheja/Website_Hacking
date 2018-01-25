from __future__ import print_function
import urllib
import sys
import logging
from prettytable import PrettyTable
import pandas
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

j = 1
z = PrettyTable()
z.field_names = ["No", "Domain Name", "Redirected To", "Response Code"]
f = open("urllist.txt")

for user in f.readlines():
	try:
		response = urllib.urlopen('http://www.' + user)
		f = response.geturl()
		v = response.code
		d = user
		dn = d[0:len(d) - 1]
		z.add_row([j, dn, f, v])
		j = j + 1
	except IOError:
		v = response.code
		f = 'NO LINK FOUND'
		d = user
		dn = d[0:len(d) - 1]
		z.add_row([j, dn, f, v])
		j = j + 1
	print(z)
print (z)



