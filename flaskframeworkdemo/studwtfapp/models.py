from .loginapp import db

class StudentModel(db.Model):
    __tablename__='studentinfo'

    id=db.Column('stud_id',db.Integer,primary_key=True)
    name=db.Column('stud_name',db.String(30),nullable=False)
    age=db.Column('stud_age',db.Integer,nullable=False)
    gender=db.Column('stud_gender',db.String(30))
    city=db.Column('stud_city',db.String(30),nullable=False)

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()