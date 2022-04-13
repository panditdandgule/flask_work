from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class EmployeeModel(db.Model):
    __init__="employees"
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(230))
    lastname=db.Column(db.String(230))
    email=db.Column(db.String(230))
    password=db.Column(db.String(230))
    gender=db.Column(db.String(230))
    country=db.Column(db.String(230))

    def __init__(self,firstname,lastname,email,password,gender,country):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.password=password
        self.gender=gender
        self.country=country

    def __repr__(self):
        return f'''{self.__dict__}'''