from config import app
from models import Product, db
from flask import request, json, jsonify


@app.route('/product/api', methods=['POST'])
def add_product():
    reqdata = request.get_json()
    if reqdata:
        prod = Product.query.filter_by(pid=reqdata.get('pid')).first()
        if prod:
            return jsonify({"Error": "Duplicate product"}), 200
        product = Product(pname=reqdata.get('pname'),
                          pqty=reqdata.get('pqty'),
                          price=reqdata.get('price'),
                          pven=reqdata.get('pven'))
        db.session.add(product)
        db.session.commit()
        return jsonify({"success": "Product added successfully"}), 201
    return jsonify({"ERROR": "Invalid Request Params..."}), 200


@app.route('/product/api', methods=['GET'])
def display_all_product():
    products = Product.query.all()

    if products:
        product_list = {}
        for prod in products:
            product_list['ProductID'] = prod.pid
            product_list['ProductName'] = prod.pname
            product_list['ProductQty'] = prod.pqty
            product_list['ProductVen'] = prod.pven

        return jsonify(product_list), 200
    else:
        return jsonify({"Error": "Products not found.."})


@app.route('/product/api/<int:pid>', methods=['GET'])
def search_product(pid):
    prod = Product.query.filter_by(pid=pid).first()
    print(prod)
    if prod:
        product_list = {}

        product_list['ProductID'] = prod.pid
        product_list['ProductName'] = prod.pname
        product_list['ProductQty'] = prod.pqty
        product_list['ProductVen'] = prod.pven

        return jsonify(product_list)
    else:
        return jsonify({"Error": "Product Not found"})


@app.route('/product/api/<int:pid>', methods=['PUT'])
def update_proudct(pid):
    requdata = request.get_json()
    prod = Product.query.filter_by(pid=pid).first()
    if prod:
        prod.pname = requdata.get('pname')
        prod.pqty = requdata.get('pqty')
        prod.price = requdata.get('price')
        prod.pven = requdata.get('pven')
        db.session.commit()
        return jsonify({"Success": "Product updated successfully"}), 200
    else:
        return jsonify({"Error": "Product not found"})


@app.route('/product/api/<int:pid>', methods=['DELETE'])
def delete_product(pid):
    prod = Product.query.filter_by(pid=pid).first()
    if prod:
        db.session.delete(prod)
        db.session.commit()
        return jsonify({"Success": "Deleted Successfully"})
    else:
        return jsonify({"Error": "Product not found for delete"})


if __name__ == '__main__':
    app.run(debug=True)
