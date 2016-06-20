# -- coding: utf-8 --
from flask import Flask,request
from subprocess import Popen
import json
from flask import send_file

app=Flask(__name__)
@app.route('/')
def index():

	pid = Popen(["venv/bin/python worker.py"], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)  
	return "ok"
@app.route("/dataWork",methods = ['POST'])
def dat():
	if request.method == 'POST':
		
		f=open("gitPush/iptv.m3u","w")
		f.write(request.data)
		f.close()
	return "ok"
@app.route("/dataGet")
def dataGet():
	return send_file("gitPush/iptv.m3u")
if __name__=="__main__":
	app.run()
