import urllib2

website ="http://www.example.com"
 
headers={}
headers['User-Agent']="Googlebot"
 
request=urllib2.Request(website,headers=headers)
response=urllib2.urlopen(request)
 
print response.read()
response.close()
 