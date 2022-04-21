from config import db


class Product(db.Model):
    __tablename__='products_info'
    id=db.Column('prod_id',db.Integer,primary_key=True)
    name=db.Column('prod_name',db.String(50))
    qty=db.Column('prod_qty',db.Integer)
    price=db.Column('prod_price',db.Float)
    vendor=db.Column('prod_vendor',db.String(80))

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all() #create table