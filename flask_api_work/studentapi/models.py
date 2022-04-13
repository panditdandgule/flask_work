from config import db


class StudentModel(db.Model):
    __tablename__='students'
    id=db.Column('stud_id',db.Integer,primary_key=True)
    name=db.Column('stud_name',db.String(30))
    age=db.Column('stud_age',db.Integer)


    def __init__(self,name,age):
        self.name=name
        self.age=age

    def json(self):
        return {
            "name":self.name,
            "age":self.age
        }

db.create_all()