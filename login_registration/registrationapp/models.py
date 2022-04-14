<<<<<<< HEAD
from config import db

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

=======
from config import db

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

>>>>>>> origin/master
db.create_all()