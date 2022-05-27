from flask import Flask,request,render_template
from flask import redirect,url_for
from flask_gtts import gtts
from werkzeug.utils import secure_filename
import os,io
import time

app=Flask(__name__)
@app.route('/driver')
def ddriver():
    return render_template('driver.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET' :
        return render_template('home.html')

@app.route('/passenger')
def driver():
    return render_template('passenger.html')

if __name__ == "__main__":
    app.run(debug=True)
