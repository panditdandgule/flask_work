from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from product_restapi.models.item import ItemModel


class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('item_url',
                        type=str,
                        required=True,
                        help="Every item needs a url."
                        )
    parser.add_argument('sizes', type=int, action='append')
    parser.add_argument('store_url',
                        type=str,
                        required=True,
                        help="Every item needs a store id!"
                        )

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(
            name=name,
            price=data['price'],
            sizes=data['sizes'],
            item_url=data['item_url'],
            store_url=data['store_url']
        )

        try:
            item.save_to_db()
        except Exception as e:
            return {"message": "An error occurred inserting the item.\n {}".format(e)}

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(
                name=name,
                price=data['price'],
                sizes=data['sizes'],
                item_url=data['item_url'],
                store_url=data['store_url']
            )
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted.'}


class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}