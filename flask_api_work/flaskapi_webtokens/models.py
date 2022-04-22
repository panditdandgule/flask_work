from config import db

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    public_id=db.Column(db.String(200))
    name=db.Column(db.String(50))
    password=db.Column(db.String(200))
    admin=db.Column(db.Boolean)

class Authors(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True,nullable=False)
    book=db.Column(db.String(20),unique=True,nullable=False)
    country=db.Column(db.String(40),nullable=False)
    booker_prize=db.Column(db.Boolean)

db.create_all()





