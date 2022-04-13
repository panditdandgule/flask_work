import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sqlalchemydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column('user_id',db.Integer,primary_key=True)
    name=db.Column('name',db.String(30))
    email=db.Column('email',db.String(30),unique=True)
    date_joined=db.Column(db.Date,default=datetime.datetime.utcnow())

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)



db.create_all()

if __name__=='__main__':
    #app.run(debug=True,port=5000)
    pass