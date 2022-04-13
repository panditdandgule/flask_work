from config import db


class Employee(db.Model):
    __tablename__='employees'

    eid=db.Column('emp_id',db.Integer,primary_key=True)
    ename=db.Column('emp_name',db.String(30),nullable=False)
    esalary=db.Column('emp_salary',db.Float)
    eage=db.Column('emp_age',db.Integer,nullable=False)
    ecity=db.Column('emp_city',db.String(30),nullable=False)


    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()