import json
from config import app
from models import Product, db
from flask import request


@app.route('/product/api/v1/<int:pid>', methods=['GET'])
def search_product(pid):
    dbproduct = Product.query.filter_by(id=pid).first()
    if dbproduct:
        product = {"PRODUCT_ID": dbproduct.id,  # after save -- id will be initialized..
                   "PRODUCT_NAME": dbproduct.name,
                   "PRODUCT_QUANTITY": dbproduct.qty,
                   "PRODUCT_PRICE": dbproduct.price,
                   "PRODUCT_VENDOR": dbproduct.vendor}
        return json.dumps({"products": product})
    else:
        return json.dumps({"Error": "Product id is not available"})


@app.route('/product/api/v1/', methods=['POST'])
def add_new_product():
    req_data = request.get_json()
    if req_data:
        name = req_data.get('name')
        if len(name) <= 2 and name.isalpha():
            return json.dumps({"Error": "Invalid Name"})
        try:
            dbproduct = Product(name=req_data.get('name'),
                                qty=req_data.get('qty'),
                                price=req_data.get('price'),
                                vendor=req_data.get('vendor')
                                )
            db.session.add(dbproduct)
            db.session.commit()
            product = {"PRODUCT_ID": dbproduct.id,  # after save -- id will be initialized..
                       "PRODUCT_NAME": dbproduct.name,
                       "PRODUCT_QUANTITY": dbproduct.qty,
                       "PRODUCT_PRICE": dbproduct.price,
                       "PRODUCT_VENDOR": dbproduct.vendor}

            return json.dumps({"Product Added successfully": product})
        except BaseException as e:
            print(e.args)
            return json.dumps({"Error": "While added product something went wrong.."})


@app.route('/product/api/v1/', methods=['GET'])
def display_all_proudcts():
    all_products = Product.query.all()
    if all_products:
        products_json = []
        for dbproduct in all_products:
            product = {"PRODUCT_ID": dbproduct.id,
                       "PRODUCT_NAME": dbproduct.name,
                       "PRODUCT_QUANTITY": dbproduct.qty,
                       "PRODUCT_PRICE": dbproduct.price,
                       "PRODUCT_VENDOR": dbproduct.vendor}
            products_json.append(product)
        return json.dumps(products_json)
    else:
        return json.dumps({"Error": "Products are not available in database.."})


@app.route('/product/api/v1/<int:pid>', methods=['PATCH'])
def update_particular_product(pid):
    req_data = request.get_json()
    if req_data:
        dbproduct = Product.query.filter_by(id=pid).first()
        if dbproduct:
            dbproduct.qty = req_data.get('qty')
            db.session.commit()
            product = {"PRODUCT_ID": dbproduct.id,  # after save -- id will be initialized..
                       "PRODUCT_NAME": dbproduct.name,
                       "PRODUCT_QUANTITY": dbproduct.qty,
                       "PRODUCT_PRICE": dbproduct.price,
                       "PRODUCT_VENDOR": dbproduct.vendor}

            return json.dumps(product)
        else:
            return json.dumps({"ERROR": "No Product with Given Id..!"})
    else:
        return json.dumps({"ERROR": "Invalid Data..!"})


@app.route('/product/api/v1/<int:pid>', methods=['PUT'])
def update_product_details(pid):
    req_data = request.get_json()
    if req_data:
        dbproduct = Product.query.filter_by(id=pid).first()
        if dbproduct:
            dbproduct.name = req_data.get('name'),
            dbproduct.qty = req_data.get('qty'),
            dbproduct.price = req_data.get('price'),
            dbproduct.vendor = req_data.get('vendor')
            db.session.commit()

            product = {"PRODUCT_ID": dbproduct.id,  # after save -- id will be initialized..
                       "PRODUCT_NAME": dbproduct.name,
                       "PRODUCT_QUANTITY": dbproduct.qty,
                       "PRODUCT_PRICE": dbproduct.price,
                       "PRODUCT_VENDOR": dbproduct.vendor}
            return json.dumps(product)
        else:
            return json.dumps({"ERROR": "No Product with Given Id..!"})
    else:
        return json.dumps({"ERROR": "Invalid Data..!"})


@app.route('/product/api/v1/<int:pid>', methods=['DELETE'])
def remove_particular_product(pid):
    product = Product.query.filter_by(id=pid).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return json.dumps({"Success": "Data Deleted successfully"})
    else:
        return json.dumps({"Error": "Provided id is not present in database."})


if __name__ == '__main__':
    app.run(debug=True)
