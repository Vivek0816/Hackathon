from flask import Flask,request,render_template
from flask import redirect,url_for
from flask_gtts import gtts
from werkzeug.utils import secure_filename
import os,io
import time

app=Flask(__name__)
@app.route('/drivertwo')
def ddriver():
    return render_template('drivertwo.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET' :
        return render_template('index.html')

@app.route('/passengertwo')
def driver():
    return render_template('passengertwo.html')

if __name__ == "__main__":
    app.run(debug=True)
