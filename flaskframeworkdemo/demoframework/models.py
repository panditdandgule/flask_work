from config import db
from sqlalchemy import or_,and_,any_

class ProductModel(db.Model):
    __tablename__ = 'productinfo'

    id = db.Column('productid', db.Integer, primary_key=True)
    name = db.Column('productname', db.String(30), nullable=False)
    qty = db.Column('productqnty', db.Integer, nullable=False)
    prc = db.Column('productprice', db.Float, nullable=False)
    ven = db.Column('productvendor', db.String(30), nullable=False)
    barcode = db.Column('productbarcode', db.String(30), unique=True)

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()
