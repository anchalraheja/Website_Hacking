from __future__ import print_function
import urllib
import sys
import logging
from prettytable import PrettyTable
import pandas
import ssl
import xlsxwriter


ssl._create_default_https_context = ssl._create_unverified_context

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)
j = 0
f = open("urllist.txt")

for user in f.readlines():
	try:
		response = urllib.urlopen('http://www.' + user)
		f = response.geturl()
		v = response.code
		d = user
		dn = d[0:len(d) - 1]
		worksheet.write(j, 0, dn)
		worksheet.write(j, 1, f)
		worksheet.write(j, 2, v)
		j = j + 1
	except IOError:
		z = 'NO LINK FOUND'
		d = user
		dn = d[0:len(d) - 1]
		v = response.code
		worksheet.write(j, 0, dn)
		worksheet.write(j, 1, 'NO LINK FOUND')
		worksheet.write(j, 2, v)
		j = j + 1



workbook.close()
