from config import db

class StudentModel(db.Model):
    __tablename__='studentsinfo'

    sid=db.Column('stud_id',db.Integer,primary_key=True)
    sname=db.Column('sutd_name',db.String(30),nullable=False)
    sage=db.Column('stud_age',db.Integer,nullable=False)
    scity=db.Column('stud_city',db.String(30),nullable=False)


    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()

