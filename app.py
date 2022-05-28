from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import redirect,url_for
from flask_gtts import gtts
from datetime import datetime
from werkzeug.utils import secure_filename
import os,io
import time
import sqlite3

app=Flask(__name__)
#con=sqlite3.connect("drivertable.db")
#print("db creation success")
#con.execute("create table Drivers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, number int UNIQUE NOT NULL, source TEXT NOT NULL, destination TEXT NOT NULL)")
##app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///drivertable.db'
##db=SQLAlchemy(app)
##app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#print("Table Created Successfully")


@app.route('/drivertwo',methods=['GET','POST'])
def ddriver():
    if request.method == 'GET':
        return render_template('drivertwo.html')

    if request.method == 'POST':
        try:

            dname=request.form['namam']
            dnumber=request.form['number']
            dsource=request.form['source']
            ddestination=request.form['dest']
            print(dname,dnumber,dsource,ddestination)
            with sqlite3.connect("drivertable.db") as con:
                cur=con.cursor()
                cur.execute("INSERT into Drivers(name,number,source,destination) values (?,?,?,?)",(dname,dnumber,dsource,ddestination))
                con.commit()
                msg="Driver added Successfully"
        except:

            con.rollback()
            msg="Couldnot add the driver"
        finally:
            return render_template('drivertwo.html',msg=msg)
            con.close()





@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET' :
        return render_template('index.html')

@app.route('/passengertwo',methods=['GET','POST'])
def driver():
    if request.method == "GET":
        return render_template('passengertwo.html')
    elif request.method == "POST":
        con = sqlite3.connect("drivertable.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from Drivers")
        rows = cur.fetchall()
        return render_template("view.html",rows = rows)





if __name__ == "__main__":
    app.run(debug=True)
