from config import db
from werkzeug.security import check_password_hash, generate_password_hash

class StudentModel(db.Model):
    __tablename__='students'
    id=db.Column('stud_id',db.Integer,primary_key=True)
    firstname=db.Column('stud_fname',db.String(30))
    lastname=db.Column('stud_lname',db.String(30))
    age=db.Column('stud_age',db.Integer)
    gender=db.Column('stud_gender',db.String(30))
    email=db.Column('stud_email',db.String(128),unique=True)
    password=db.Column('stud_password',db.String(128))
    hobbies=hobbies=db.Column('stud_hobbies',db.String(30))
    country=country=db.Column('stud_country',db.String(30))



    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)



    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

db.create_all()