from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__="employee"
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(30))
    lname=db.Column(db.String(30))
    age=db.Column(db.Integer())
    city=db.Column(db.String(200))


    def __init__(self,fname,lname,age,city):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.city=city

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)