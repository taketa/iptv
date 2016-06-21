# -- coding: utf-8 --
from flask import Flask,request
from subprocess import Popen
import json
from flask import send_file

app=Flask(__name__)
@app.route("/",methods = ['GET','POST'])
def dat():
	if request.method == 'POST':
		
		f=open("iptv.m3u","w")
		f.write(request.data)
		f.close()
	
	return "ok"
@app.route("/get")
def dataGet():
	return send_file("iptv.m3u")
if __name__=="__main__":
	app.run()
