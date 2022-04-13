from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.secret_key="studcrudapplication"

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/stud_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)