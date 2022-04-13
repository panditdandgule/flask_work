from config import db

class Product(db.Model):
    __tablename__='products'
    id = db.Column("product_id",db.Integer,primary_key=True)
    name = db.Column("product_name",db.String(30),nullable=False)
    qty = db.Column("product_quantity",db.Integer)
    prc = db.Column("product_price",db.Float)  #float ---> mysql --> sqlalchemy
    ven = db.Column("product_vendor",db.String(30),nullable=False)
    barcode = db.Column("product_barcode",db.String(30),unique=True)


    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

db.create_all()