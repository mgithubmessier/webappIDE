from flask import Flask
from flask import abort, redirect, url_for
from flask import request
from flask import render_template
from flask import session
import cgi
import cgitb
import os
import logging
import sys
import smtplib
from subprocess import call
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('root'))

@app.route('/root', methods=['POST', 'GET'])
def root():
    compData = ''
    if request.method == 'POST':

        print "Hi"

        if 'text' in request.form:
            #obtains contents of the "text" form from index.html
            code = str(request.form['text'])

            #prints code from the "text" form from index.html
            print(str(code))

            #call is for calling a command in the terminal
            #this is a test case for what will be the "javac" command
            call(["echo",str(code)])
            #writes out '256' for some reason
            compData = str(compileJava(str(code)))
        return render_template('index.html', **locals())
    return render_template('index.html')

def compileJava(code):
    print('echo \"'+str(code)+'\" > toCompile.java')
    os.system('echo \"'+ str(code)+ '\" > toCompile.java ')
    #subprocess.Popen('echo \"'+str(code)+'\" > toCompile.java')
    #call(["echo",str(code),"> toCompile.java"])
    os.system("javac toCompile.java 2> console.txt")

    scanner = open('console.txt','r')
    compilation = scanner.read()
    scanner.close()
    return compilation

if __name__ == "__main__":
    app.secret_key = 'jykasgAKUJRkyt5456^%438z'
    app.run(host='0.0.0.0', debug=True)
