# -- coding: utf-8 --
#!venv/bin/python
from flask import Flask,request
from subprocess import Popen
import json
from flask import send_file

app=Flask(__name__)
<<<<<<< HEAD
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
=======
@app.route('/')
def index():

	pid = Popen(["python worker.py"], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)  
	return "ok"

>>>>>>> 43c9413c3308b0083729e89dd2b2bb01c88fad5e
if __name__=="__main__":
	app.run()
