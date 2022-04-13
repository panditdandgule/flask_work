from config import app
from flask import request, render_template
from models import *
from productservices import ProductServices

@app.route('/save', methods=['GET', 'POST'])
def add_product_in_stock():
    message = ''
    if request.method == 'GET':
        return render_template('product.html')

    if request.method == 'POST':
        formdata = request.form

        prodid = ProductModel.query.filter_by(id=formdata.get('id')).first()
        if prodid:
            message = "Duplicate product id"
        else:
            try:
                product = ProductModel(id=formdata.get('productid'),
                                       name=formdata.get('productname'),
                                       qty=formdata.get('productquantity'),
                                       prc=formdata.get('productprice'),
                                       ven=formdata.get('productvendor'),
                                       barcode=formdata.get('productbarcode')
                                       )
                db.session.add(product)
                db.session.commit()
                message = "Product Added successfully"
            except BaseException as e:
                message = e.args[1]
    return render_template('product.html', message=message)

@app.route('/<int:id>/update',methods=['GET','POST'])
def modify_existing_product_details(id):
    product=ProductModel.query.filter_by(id=id).first()
    if request.method=='POST':
        formdata=request.form
        db.session.delete(product)
        db.session.commit()
        if product:
            id=formdata.get('productid')
            name=formdata.get('productname')
            qty=formdata.get('productquantity')
            prc=formdata.get('productprice')
            ven=formdata.get('productvendor')
            barcode=formdata.get('productbarcode')

            product=ProductModel(id=id,
                                 name=name,
                                 qty=qty,
                                 prc=prc,
                                 ven=ven,
                                 barcode=barcode)
            db.session.add(product)
            db.session.commit()
        return f'''product id with {id} does not exists'''
    return render_template('update.html',product=product)



@app.route('/display',methods=['GET'])
def fetch_list_of_products():
    products=ProductModel.query.all()
    return render_template('display.html',products=products)

if __name__ == '__main__':
    app.run(debug=True)
