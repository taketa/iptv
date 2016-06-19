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
        m3=open("git/forTest.m3u")
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
        
        f=open('git/nStream.xml','w')
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n<items>\n<playlist_name>IPTV</playlist_name>\n<all_region></all_region>\n')
        f.close()
        f=open('git/nStream.xml','a')
        for i in good:
            f.write("<channel>\n<title><![CDATA[%s]]></title>\n<logo_30x30><![CDATA[]]></logo_30x30>\n<description></description>\n<stream_url><![CDATA[%s]]></stream_url>\n</channel>\n" % (i,good[i])) 
        f.close()

        # call(["git","add","."])
        # call(["git","commit","-am","'ok'"])
        # call(["ssh-add"])
        # call(["git","push","-u","origin","master"])
        f=open('git/iptv.m3u', 'w')
        f.write("#EXTM3U\n")
        f.close()
        for i in good:
            f=open('git/iptv.m3u', 'a')
            f.write("#EXTINF:-1,"+i+"\n"+good[i]+"\n")
            f.close()
        ssh=open(".ssh/id_rsa.pub","w")
        ssh.write("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5uihQFeVnpj+ZapmKFJO1K5AjTBujXs22wN+yJklx0YCI7statYU0oyhs8cBKG09V+fhFYSLZA494furJqI+k+h7O1ho8PSf+iDTauiP8V9kyniAiJ0FabSU/pnooxMOVtxmpjBqHGp2MYYiYKzzsSxusYbK6xo4gOaWZzbPy5v8rBsIGbQh1mcw/Jy+81PkwmtULFY58UXTBRjSV+pcK+LG9OEJqa5QRzcnEHq98lsx424QrcVexHyllzmlWq8Qwgvz7cHUpXsZWmIF0xT9yUW7UEKJsXbv8AJdlxULbU9ExQcu/6xCf8fOuZfMH7iBJrauXYSQT7wfaKrAvTS6j taketa@taketa")
        ssh.close()
        os.chdir("git")
        
        
        call(["git", "remote", "add", "taketa", "git@github.com:taketa/iptv.git"])
        call(["git","add","."]) 
        call(["git","commit","-am","ok"])
        call(["git","pull","taketa","master"])
        
        

        call(["git","push","-u","taketa","master"])
        return 
    getm3()

   
    return "ok"
    # return send_file('iptv.m3u')
    








if __name__=="__main__":
	app.run()
