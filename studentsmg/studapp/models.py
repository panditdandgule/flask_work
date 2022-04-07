from student import db

#one-to-one relationship
class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    father=db.relationship('Father',backref='student',uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.father:
            return f'Student name is {self.name},id is {self.id} and father name is {self.father.name}'
        else:
            return f'Student name is {self.name},id is {self.id} and father name is not available'

class Father(db.Model):
    __tablename__='fathers'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    student_id=db.Column(db.Integer,db.ForeignKey('students.id'))


    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id

    def __repr__(self):
        return f"Father name:{self.name}"

db.create_all()
