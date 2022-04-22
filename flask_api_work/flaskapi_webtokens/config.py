from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET_KEY']="Th1s1sskjldf"
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/webtoken_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


