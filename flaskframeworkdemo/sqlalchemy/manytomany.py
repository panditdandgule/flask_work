from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sqlalchemydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

user_channel=db.Table('user_channel',db.Column('user_id',db.Integer,db.ForeignKey('users.user_id')),
                                     db.Column('ch_id',db.Integer,db.ForeignKey('channel.ch_id')))


class Users(db.Model):
    id=db.Column('user_id',db.Integer,primary_key=True)
    name=db.Column('name',db.String(30))
    following=db.relationship('Channel',secondary=user_channel,backref='followers')

class Channel(db.Model):
    id=db.Column('ch_id',db.Integer,primary_key=True)
    name=db.Column('name',db.String(30))

db.create_all()