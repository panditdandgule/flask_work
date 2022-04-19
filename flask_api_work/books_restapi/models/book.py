from books_restapi.database import db


class BookModel(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    publication = db.Column(db.String(20), nullable=False)

    def __init__(self, name, price, publication):
        self.name = name
        self.price = price
        self.publication = publication

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'publication': self.publication

        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


'''
find_by_name : searches for a book name provided by user and returns that row from database if such a book present. It is a class method.
add_to_db : adds and saves the data in the object to the database.
delete_from_db : removes the data in the object from database.
'''
