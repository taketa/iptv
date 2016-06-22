# -- coding: utf-8 --
#!venv/bin/python
from flask import Flask,request
from subprocess import Popen
import json
from flask import send_file

app=Flask(__name__)
@app.route('/')
def index():

	pid = Popen(["python worker.py"], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)  
	return "ok"

if __name__=="__main__":
	app.run()
