from config import db

class Employee(db.Model):
    __tablename__='employee_info'
    id=db.Column('emp_id',db.Integer,primary_key=True)
    name=db.Column('emp_name',db.String(120))
    age=db.Column('emp_age',db.Integer)
    salary=db.Column('emp_salary',db.Float)

db.create_all()