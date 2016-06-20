# -- coding: utf-8 --

from subprocess import call
import urllib2
from subprocess import Popen, PIPE
import re 
import datetime
import os

def pushHer():
	call("yes|ssh-keygen -f /app/.ssh/id_rsa -t rsa -N ''",shell=True)
	ssh=open("/app/.ssh/id_rsa.pub")
	ssh=ssh.readline().rstrip()
	call('curl -u "taketa:weuwdfyu7" --data \'{"title":"test-key","key":"%s"}\' https://api.github.com/user/keys' % ssh,shell=True)
	# call("eval 'ssh-agent -s'",shell=True)
	# call("ssh-add ~/.ssh/id_rsa",shell=True)

	# call("yes|ssh -T git@github.com",shell=True)
	

	

	# call("eval $(ssh-agent)",shell=True)
	
	
	
	
	

	
	os.chdir("gitPush")
	call("git init",shell=True)
	call("git remote add origin git@github.com:taketa/iptv.git",shell=True)
	call("git add .",shell=True)
	call('git config --global user.email "853211b@gmail.com" && git config --global user.name "Your Name"',shell=True) 
	call("git pull origin master",shell=True)
	call('git commit -am "ok"',shell=True)
	call("git pull origin master",shell=True)
	call('git commit -am "ok"',shell=True)
	call("git push origin master",shell=True)
	return "ok"
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
pushHer()