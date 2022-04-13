from dbconfig import db


class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    salary = db.Column(db.Float)

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)

    def json(self):
        return {
            "name":self.name,
            "email":self.email,
            "salary":self.salary
        }

db.create_all()
