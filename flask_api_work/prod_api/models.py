from config import db


class Product(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    pname=db.Column(db.String(40))
    pqty=db.Column(db.Integer)
    price=db.Column(db.Float)
    pven=db.Column(db.String(50))

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()