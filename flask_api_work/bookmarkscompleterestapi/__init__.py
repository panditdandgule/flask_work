from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from auth import auth
from bookmark import bookmark
from flask_jwt_extended import JWTManager

app=Flask(__name__,instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/emptest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

app.register_blueprint(auth)
app.register_blueprint(bookmark)
JWTManager(app)
