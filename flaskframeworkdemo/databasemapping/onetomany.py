from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3305/onetomany'
app.config["SQLALCHEMY_ECHO"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def one_to_many():
    class Employee(db.Model):
        id = db.Column('emp_id', db.Integer, primary_key=True)
        name = db.Column('emp_name', db.String(40))
        age = db.Column('emp_age', db.Integer)
        address = db.relationship("Address", backref="emp_ref",uselist=True)  # list of Address model

    class Address(db.Model):
        id = db.Column('adr_id', db.Integer, primary_key=True)
        city = db.Column('city', db.String(40))
        pincode = db.Column('pincode', db.Integer)
        e_id = db.Column("em_id", db.ForeignKey("employee.emp_id"), unique=False, nullable=True)
        #emp_ref will come here

    db.create_all()

if __name__=='__main__':
    one_to_many()
    #app.run(debug=True)