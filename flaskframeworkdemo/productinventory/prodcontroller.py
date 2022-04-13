from config import app
from config import db
from models import Product
from flask import request, render_template


@app.route('/')
@app.route('/product')
def home():
    return render_template('index.html', flag=False)


@app.route('/product/save', methods=['POST', 'GET'])
def save():
    message = ''
    if request.method == 'POST':
        formdata = request.form

        dbprod = Product.query.filter_by(id=formdata.get('pid')).first()

        if dbprod:
            dbprod.name = formdata.get('pname')
            dbprod.qty = formdata.get('pqty')
            dbprod.prc = formdata.get('pprc')
            dbprod.ven = formdata.get('pven')
            dbprod.barcode = formdata.get('pbar')
            db.session.commit()
            message = "Product Updated successfully.."
        else:
            try:
                product = Product(id=formdata.get('pid'),
                                  name=formdata.get('pname'),
                                  qty=formdata.get('pqty'),
                                  prc=formdata.get('pprc'),
                                  ven=formdata.get('pven'),
                                  barcode=formdata.get('pbar'))
                db.session.add(product)
                db.session.commit()
                message = 'Product Added Successfully..'
            except BaseException as e:
                message = e.args[1]
    dummy = Product(id=0, name="", qty=0, prc=0.0, ven="", barcode="")
    return render_template('save.html', result=message, d_product=dummy)


@app.route('/product/display', methods=['GET', 'Post'])
def display():
    products = Product.query.all()
    return render_template('display.html', products=products)


@app.route("/product/edit/<int:prid>")
def update_product(prid):
    dbproduct = Product.query.filter_by(id=prid).first()  # id se-- retrive
    if dbproduct:
        return render_template('save.html', d_product=dbproduct)


@app.route('/product/delete/<int:prid>')
def delete_product(prid):
    dbproduct = Product.query.filter_by(id=prid).first()
    if dbproduct:
        db.session.delete(dbproduct)
        db.session.commit()

    products = Product.query.all()
    return render_template('display.html', products=products)


@app.route('/product/search', methods=['GET', 'POST'])
def search_product():
    products = None
    if request.method == 'POST':
        user_selection = request.form.get('search')
        user_input = request.form.get('inputval')
        if user_selection == 'ID':
            products = Product.query.filter_by(id=user_input).first()
        elif user_selection == 'NAME':
            products = Product.query.filter(Product.name == user_input).all()
        elif user_selection == 'VENDOR':
            products = Product.query.filter(Product.ven == user_input).all()

    return render_template('index.html', flag=True, products=products)


if __name__ == '__main__':
    app.run(debug=True)
