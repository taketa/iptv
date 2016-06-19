# -- coding: utf-8 --
from flask import Flask
from subprocess import Popen


app=Flask(__name__)
@app.route('/')
def index():
    pid = Popen(["python worker.py"], shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)  
    return "ok"

if __name__=="__main__":
	app.run()
