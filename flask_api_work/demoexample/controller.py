from config import app
from models import ProductModel
from config import db
from flask_restful import Api, Resource, request, reqparse

api = Api(app)


class ProductView(Resource):
    '''
    parser=reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="Can't leave blank"
                        )
    parser.add_argument('price',
                        type='float',
                        required=True,
                        help="Can't leave blank")
    parser.add_argument('brand',
                        type=str,
                        required=True,
                        help="Can't leave blank")
    '''

    def get(self):
        products = ProductModel.query.all()
        return {'Products': list(x.json() for x in products)}

    def post(self):
        data = request.get_json()
        new_product = ProductModel(data['name'], data['description'], data['price'], data['brand'])
        db.session.add(new_product)
        db.session.commit()
        db.session.flush()

        return new_product.json(), 201


class SingleProductView(Resource):
    def get(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if product:
            return product.json()
        return {'message': 'Product id not found'}, 404

    def delete(self, id):
        product = ProductModel.query.filter_by(id=id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Deleted'}
        else:
            return {'message': 'Product not found'}, 404

    def put(self, id):
        data = request.get_json()
        product = ProductModel.query.filter_by(id=id).first()

        if product:
            product.name = data['name']
            product.price = data['price']
            product.description = data['description']
            product.brand = data['brand']
        else:
            product = ProductModel(id=id, **data)

        db.session.add(product)
        db.session.commit()

        return product.json()


api.add_resource(ProductView, '/products')
api.add_resource(SingleProductView, '/product/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
