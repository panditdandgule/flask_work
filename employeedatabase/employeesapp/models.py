from config import db

class Employee(db.Model):
    __tablename__='employees'
    id=db.Column("emp_id",db.Integer,primary_key=True)
    name=db.Column('emp_name',db.String(30))
    age=db.Column('emp_age',db.Integer)
    address=db.relationship('Address',backref='empref',uselist=True,lazy=True)

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

class Address(db.Model):
    aid=db.Column('addr_id',db.Integer,primary_key=True)
    city=db.Column('City',db.String(30))
    country=db.Column('Country',db.String(30))
    e_id=db.Column('emp_id',db.Integer,db.ForeignKey('employees.emp_id'))

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()