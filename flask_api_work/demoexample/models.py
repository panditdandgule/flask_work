from config import db


class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column('prod_id', db.Integer, primary_key=True)
    name = db.Column('prod_name', db.String(30))
    description = db.Column('prod_desc', db.String(255))
    price = db.Column('prod_prc', db.Integer)
    brand = db.Column('prod_brand', db.String(80))

    def __init__(self, name, description, price, brand):
        self.name = name
        self.description = description
        self.price = price
        self.brand = brand

    def json(self):
        return {
                "name": self.name,
                "description": self.description,
                "price": self.price,
                "brand": self.brand
                }


