from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class UsersModel(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(230))
    email=db.Column(db.String(230))
    password=db.Column(db.String(230))
    city=db.Column(db.String(230))

    def __init__(self,name,email,password,city):
        self.name=name
        self.email=email
        self.password=password
        self.city=city

    def __str__(self):
        return f'''{self.__dict__}'''
