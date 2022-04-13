from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3305/new_db'
app.config["SQLALCHEMY_ECHO"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def one_to_one():
    class Employee(db.Model):
        id=db.Column('emp_id',db.Integer,primary_key=True)
        name=db.Column('emp_name',db.String(40))
        age=db.Column('emp_age',db.Integer)
        address=db.relationship('Address',backref='emp_ref',uselist=False,lazy=False)#one to one relationshp uselist=False

    class Address(db.Model):
        id=db.Column('addr_id',db.Integer,primary_key=True)
        city=db.Column('city',db.String(40))
        pincode=db.Column('pincode',db.Integer)
        e_id=db.Column('emp_id',db.ForeignKey('employee.emp_id'),unique=True,nullable=True)

    db.create_all()

    # e1 = Employee(id=101,name='AAAA',age=23)
    # e2 = Employee(id=102, name='BBBB', age=21)
    #
    # ad1 = Address(id=1,city="Pune",pincode=233333,e_id=e1.id)
    # ad2 = Address(id=2,city="Mumbai",pincode=21212,e_id=e2.id) #unique-True
    #
    # db.session.add_all([e1,e2])
    # db.session.commit()
    #
    # db.session.add_all([ad1,ad2])
    # db.session.commit()

    emp = Employee.query.filter_by(id=101).first()
    print(emp.__dict__)

    print('--------------------------------------------------------')
    print(emp.address.__dict__) # explicitly demand

    adr = Address.query.filter_by(id=1).first()
    print(adr.__dict__)
    print(adr.emp_ref.__dict__)

if __name__=='__main__':

    one_to_one()
    #app.run(debug=True,port=5000)