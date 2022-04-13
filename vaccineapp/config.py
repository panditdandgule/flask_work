from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY']='vaccineapplication'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/vaccinedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)