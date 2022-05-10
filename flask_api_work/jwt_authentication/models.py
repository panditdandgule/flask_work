from config import db


class Account(db.Model):
    __tablename__='account'
    id = db.Column('id',db.Integer, primary_key=True)
    balance = db.Column('acc_balace',db.Float)
    type = db.Column('acc_type',db.String(30))
    cust_id = db.Column('cust_id',db.ForeignKey('customer.id'),unique=False)
    #customer


class Customer(db.Model):   #customer.query.filter_by(id=101).first()  customer.accounts
    __tablename__='customer'
    id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name',db.String(30))
    username = db.Column('username',db.String(80), unique=True)
    password = db.Column('password',db.String(120))
    email = db.Column('email',db.String(80), unique=True)
    accounts = db.relationship(Account,lazy=False,backref='customer')
    #accounts = db.relationship(Account, lazy=False, backref='customer')

db.create_all()

