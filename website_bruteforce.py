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