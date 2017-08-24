import threading
import os
import Queue
import urllib2

threads=10
url="http://www.example.com"
wordlist=""
user-agent ="Googlebot"
resume = None

def build_wordlist(wordlist):
    fileopen= open("wordlist","rb")
    line=fileopen.readlines()
    fileopen.close()
    
    found_resume = False
    words = Queue.Queue()
    
    for word in line:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume= True
                    print "Resuming list from %s" % resume
        else:
            words.put(word)
    return words

def directory_bruteforce(word_queue,extensions=None):
    
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s/" % attempt)
            
        if extensions:
            for extensions in extensions:
                attempt_list.append("/%s%s" % (attempt,extensions))
        
        for brute in attempt_list:
            url2 = "%s%s" % (url,urllib2.quote(brute))
            try:
                headers={}
                headers["User-Agent"] = user-agent
                r = urllib2.Request(url,headers= headers)
                
                response =urllib2.urlopen(r)
                if len(response.read()):
                    print "[%d] => %s" % (response.code,url2)
                    
                except urllib2.URLError,e:
                    if hasattr(e,'code') and e.code != 404:
                        print  "%d => %s" % (e.code,url)
                        
                    pass