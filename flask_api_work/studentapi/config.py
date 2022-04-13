from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/studapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)


db=SQLAlchemy(app)
