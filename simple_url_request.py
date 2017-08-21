import urllib2

website=urllib2.urlopen("http://www.example.com")

print website.read()