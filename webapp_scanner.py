import os
import threading
import Queue
import urllib2

threads=10

target="http://www.example.com"
directory="/Users/root1/Downloads/Joomla_3.7.5-Stable-Full_Package"
filters=[".jpg",".png",".css",".gif"]

os.chdir(directory)
web_paths = Queue.Queue()

for r,d,f in os.walk("."):
    for files in f:
        remote_path = "%s%s" % (r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)
def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url ="%s%s" % (target,path)
        
        request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
        content = response.read()
        
        print "[%d] => %s" % (response.code,path)
        
    except urllib2.HTTPError as error:
        print "failed %s" % error.code
        pass
    
for i in range(threads):
    print "Spawning thread: %d" % i
    t=threading.Thread(target=test_remote)
    t.start()