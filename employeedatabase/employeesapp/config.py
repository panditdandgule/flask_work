from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY'] = "knowledgedatae"
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/employee_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

Migrate(app,db)
