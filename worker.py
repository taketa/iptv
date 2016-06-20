# -- coding: utf-8 --
from flask import request,url_for
from subprocess import call
import urllib2
from subprocess import Popen, PIPE
import re 
import datetime
import os
import requests
import json

def push():
	f=open('gitPush/iptv.m3u')
	
	r = requests.post("https://safe-shore-24742.herokuapp.com/data", data=f)
	f.close()
def run(url):
	p = Popen(["timeout","20s","ffprobe",  url], stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	test=re.findall(',\s.*kb/s',stderr)
	if test: return "good"
	else: return "bad"
def getm3(url="http://iptv.slynet.tv/FreeSlyNet.m3u"):
    m3=open("gitPush/forTest.m3u")
    # m3=urllib2.urlopen(url)
    m3=m3.read()    
    out=m3.split("\n#EXTINF:-1,")
    out=[i.split("\n") for i in out if "PremiumSlyNet" not in i]
    out=[i for i in out if len(i)==2]
    out=[i for i in out if "===" not in i[0]]
    good={}  
    for i in out:
        test=run(i[1].split(" ")[0])
        print(test)
        print(i[1].split(" ")[0])
        if test=="good":
            good[i[0]]=i[1]
    
	f=open('gitPush/nStream.xml','w')
	f.write('<?xml version="1.0" encoding="UTF-8" ?>\n<items>\n<playlist_name>IPTV</playlist_name>\n<all_region></all_region>\n')
	f.close()
	f=open('gitPush/nStream.xml','a')
	for i in good:
		f.write("<channel>\n<title><![CDATA[%s]]></title>\n<logo_30x30><![CDATA[]]></logo_30x30>\n<description></description>\n<stream_url><![CDATA[%s]]></stream_url>\n</channel>\n" % (i,good[i])) 
	f.close()
	f=open('gitPush/iptv.m3u', 'w')
	f.write("#EXTM3U\n")
	f.close()
	f=open('gitPush/iptv.m3u', 'a')
	for i in good:
	    
	    f.write("#EXTINF:-1,"+i+"\n"+good[i]+"\n")
	f.close()
	
	
    return "ok"

getm3()
push()