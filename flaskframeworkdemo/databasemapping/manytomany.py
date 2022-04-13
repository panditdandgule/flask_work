from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3305/manytomany'
app.config["SQLALCHEMY_ECHO"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def many_to_many():
    emp_adr_mapping = db.Table("emp_adr_mapping",
                               db.Column('emp_id', db.Integer, db.ForeignKey("employee.emp_id"),unique=False),
                               db.Column('adr_id', db.Integer, db.ForeignKey("address.adr_id"),unique=False)
                               )

    class Employee(db.Model):
        id = db.Column('emp_id', db.Integer, primary_key=True)
        name = db.Column('emp_name', db.String(40))
        age = db.Column('emp_age', db.Integer)
        #adr_list

    class Address(db.Model):
        id = db.Column('adr_id', db.Integer, primary_key=True)
        city = db.Column('city', db.String(40))
        pincode = db.Column('pincode', db.Integer)
        emp_list = db.relationship('Employee', secondary=emp_adr_mapping,backref=db.backref('adr_list', lazy=True))

    db.create_all()

    e1 = Employee(id=101, name='AAAA', age=23)
    e2 = Employee(id=102, name='BBBB', age=21)
    e3 = Employee(id=103, name='CCCC', age=24)
    db.session.add_all([e1, e2,e3])
    db.session.commit()

    ad1 = Address(id=1, city="Pune", pincode=233333)
    ad2 = Address(id=2, city="Mumbai", pincode=21212)
    db.session.add_all([ad1, ad2])
    db.session.commit()

    #3rd table insertation
    e1.adr_list.extend([ad1,ad2])
    e2.adr_list.extend([ad1,ad2])
    e3.adr_list.extend([ad1,ad2])

    db.session.commit()
    #ad1 --> e1 e2 e3  --->  e1 -->> ad1 ad2

if __name__ == '__main__':

    print('=====')
    many_to_many()
