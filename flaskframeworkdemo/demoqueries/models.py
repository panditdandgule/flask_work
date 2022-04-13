from config import db
from config import app
from sqlalchemy import all_,or_,and_,any_
from sqlalchemy import desc
from sqlalchemy import func

class ProductsModel(db.Model):
    __tablename__ = 'products'
    pid = db.Column('product_id', db.Integer, primary_key=True)
    pname = db.Column('product_name', db.String(30), nullable=False)
    pqty = db.Column('product_quantity', db.Integer, nullable=False)
    pprc = db.Column('product_price', db.Float, nullable=False)
    pven = db.Column('product_vendor', db.String(30), nullable=False)
    pbarcod = db.Column('product_barcode', db.String(30), unique=True)

    def __str__(self):
        return f'''\n{self.__dict__}'''

    def __repr__(self):
        return str(self)


db.create_all()
#Insert one record into database
# p=ProductsModel(pid=110,pname="Laptop",pqty=3,pprc=44443.34,pven="Amazon",pbarcod="@)Sl#*+#")
# db.session.add(p)
# db.session.commit()
#Insert records into databases
# p1 = ProductsModel(pid=104,pname="MObile",pqty=23,pprc=283.34,pven="Flipkart",pbarcod="@)SK#*##")
# p3 = ProductsModel(pid=105,pname="MObile",pqty=243,pprc=9283.34,pven="Flipkart",pbarcod="@*4(SK#*(##")
# p4 = ProductsModel(pid=106,pname="MObile",pqty=253,pprc=2883.34,pven="Flipkart",pbarcod="@*5SK#*(##")
# p5 = ProductsModel(pid=107,pname="MObile",pqty=263,pprc=2873.34,pven="Flipkart",pbarcod="6@*(SK#*(##")
# db.session.add_all([p1,p3,p4,p5])
# db.session.commit()



# Display all products
# products=ProductsModel.query.all()
# print(products)

#search product
#product=ProductsModel.query.filter_by(pid=103).first()
#print(product)

#Delete product
# product=ProductsModel.query.filter_by(pid=108).first()
# db.session.delete(product)
# db.session.commit()
# print()
# print(product,"Record deleted successfully")

#Find particular prdouct with their names
#productName=ProductsModel.query.filter(ProductsModel.pname=='Mobile').all()
#print(productName)

# productName=ProductsModel.query.filter(ProductsModel.pname=='Laptop').all()
# print(productName)

#Find particular product names only two
# products=ProductsModel.query.filter(and_(ProductsModel.pname=='Mobile',ProductsModel.pven=='Flipkart')).all()[:2]
# print(products)

# products=ProductsModel.query.filter(or_(ProductsModel.pname=='Laptop',ProductsModel.pven=='Amazon')).all()
# print(products)

#select queries
# products=ProductsModel.query.filter(ProductsModel.pname.endswith('op')).all()
# print(products)

#Orderining user by something
# products=ProductsModel.query.order_by(ProductsModel.pname).all()
# print(products)

#Limiting users
# products=ProductsModel.query.limit(4).all()
# print(products)

#Getting query by primary key
# products=ProductsModel.query.get(104)
# print(products)

# products=ProductsModel.query.filter_by(pid=114).first_or_404()
# print(products)

#Filter query sql alchemy
# products=ProductsModel.query.all()
# print(products)
# products=ProductsModel.query.filter(ProductsModel.pid==104).all()
# print(products)

#multiple conditions
# products=ProductsModel.query.filter(ProductsModel.pname=='Laptop',ProductsModel.pven=='Flipkart').all()
# print(products)

#Like Query
# products=ProductsModel.query.filter(ProductsModel.pname.like('M%')).all()
# print(products)
# products=ProductsModel.query.filter(ProductsModel.pname.like('%e')).all()
# print(products)

# products=ProductsModel.query.filter(ProductsModel.pname.like('%p')).all()
# print(products)

# products=ProductsModel.query.filter(ProductsModel.pname.like('L%')).all()
# print(products)

#Get first record
# products=ProductsModel.query.filter(ProductsModel.pid>104).all()
# print(products)
# products=ProductsModel.query.filter(ProductsModel.pid>104).first()
# print(products)

#Using Like operator
#record has 'Mobile' keyword on any position
# products=ProductsModel.query.filter(ProductsModel.pname.like('%Mobile%')).all()
# print(products)
#record has 'Mobile' keyword on first position
# products=ProductsModel.query.filter(ProductsModel.pname.like('%Mobile')).all()
# print(products)
#record has 'Mobile' keyword on last position
# products=ProductsModel.query.filter(ProductsModel.pname.like('Mobile%')).all()
# print(products)

#Delete query
# products=ProductsModel.query.filter(ProductsModel.pid==107).delete()
# db.session.commit()
# print("Deleted successfully..")

#Update columns
# products=ProductsModel.query.filter_by(pid=106).first()
# print("Before update",products)
# products=ProductsModel.query.filter(ProductsModel.pid==106).update({ProductsModel.pname:'Laptop',
#                                                                     ProductsModel.pven:'Amazon'})
# db.session.commit()
# print(products)

#using order by keyword
# products=ProductsModel.query.order_by(desc(ProductsModel.pid)).all()
# print(products)

# vendor_counts=ProductsModel.query.group_by(ProductsModel.pven).all()
# print(vendor_counts)

#and query
# products=ProductsModel.query.filter(and_(ProductsModel.pname=='Laptop',ProductsModel.pven=='Amazon')).all()
# print(products)

#or query
# products=ProductsModel.query.filter(or_(ProductsModel.pname=='Laptop',ProductsModel.pven=='Flipkart')).first()
# print(products)

#in query
# products=ProductsModel.query.filter(ProductsModel.pid.in_((103,102))).all()
# print(products)

# products=ProductsModel.query.filter(ProductsModel.pid.in_((102,103,104))).all()
# print(products)

# #distinct record
# products=ProductsModel.query.distinct().all()
# print(products)

#Get highest id or value record from a column SqlAlchemy Query
# products=ProductsModel.query.filter(func.max(ProductsModel.pprc)).all()
# print(products)

if __name__ == '__main__':
    app.run(debug=True)
