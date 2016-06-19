# -- coding: utf-8 --
from flask import render_template, request, jsonify, Flask
import json
from langdetect import detect_langs
from flask import send_file
from subprocess import call
import urllib2
from subprocess import Popen, PIPE
import re 
import datetime
import os

app=Flask(__name__)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

# шифрование

    return jsonify(result="Caesar said that the text is not encrypted")
@app.route('/')
def list():
    def run(url):
        p = Popen(["timeout","20s","ffprobe",  url], stdout=PIPE, stderr=PIPE)
        # "-v","error",
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
        
        f=open('nStream.xml','w')
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n<items>\n<playlist_name>IPTV</playlist_name>\n<all_region></all_region>\n')
        f.close()
        f=open('gitPush/nStream.xml','a')
        for i in good:
            f.write("<channel>\n<title><![CDATA[%s]]></title>\n<logo_30x30><![CDATA[]]></logo_30x30>\n<description></description>\n<stream_url><![CDATA[%s]]></stream_url>\n</channel>\n" % (i,good[i])) 
        f.close()

    
        f=open('gitPush/iptv.m3u', 'w')
        f.write("#EXTM3U\n")
        f.close()
        for i in good:
            f=open('gitPush/iptv.m3u', 'a')
            f.write("#EXTINF:-1,"+i+"\n"+good[i]+"\n")
            f.close()
        os.chdir("gitPush")
        call("git  init",shell=True)
        call("ssh-keygen -f /app/.ssh/id_rsa -t rsa -N '' -y",shell=True)
        ssh=open("../.ssh/id_rsa.pub")
        ssh=ssh.readline().rstrip()
        call('curl -u "taketa:weuwdfyu7" --data \'{"title":"test-key","key":"%s"}\' https://api.github.com/user/keys' % ssh,shell=True)
        
        call("git remote add origin git@github.com:taketa/iptv.git",shell=True)
        call("git add iptv.m3u nStream.xml",shell=True)
       
        call('git config --global user.email "you@example.com" && git config --global user.name "Your Name"',shell=True) 
        
       
        call("git pull origin master",shell=True)
		call('git commit -am "ok"',shell=True)
        
        

        call("git push origin master",shell=True)
        return "ok"
    getm3()

   
    return "ok"
    # return send_file('iptv.m3u')
    








if __name__=="__main__":
	app.run()
