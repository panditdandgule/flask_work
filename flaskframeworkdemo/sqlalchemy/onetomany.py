import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sqlalchemydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Owner(db.Model):
    id=db.Column('owner_id',db.Integer,primary_key=True)
    name=db.Column('name',db.String(30))
    address=db.Column('address',db.String(30))
    pets=db.relationship('Pet',backref='owner')

class Pet(db.Model):
    id=db.Column('pet_id',db.Integer,primary_key=True)
    name=db.String('name',db.String(30))
    age=db.Column(db.Integer)
    ow_id=db.Column('owner_id',db.Integer,db.ForeignKey('owner.owner_id'),unique=False)

db.create_all()
