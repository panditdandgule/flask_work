from product_restapi.db import db
from product_restapi.models.store import StoreModel

class ItemModel(db.Model):
    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    sizes = db.Column(db.String(80))
    item_url = db.Column(db.String)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, sizes, store_url, item_url):
        self.name = name
        self.price = price
        self.sizes = sizes
        self.item_url = item_url

        self.store_url = store_url
        # set dynamically from ^
        self.store_id = self.get_store_id(store_url)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'sizes': self.sizes,
            'item_url': self.item_url,
            'store_id': self.store_id
        }

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_store_id(store_url):
        return StoreModel.get_store_id(store_url)