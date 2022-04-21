from flask_jwt import jwt_required
from flask_restful import Resource

from product_restapi.models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'store already exists in the database.'}, 400

        # else create a new store
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store.'}, 500

        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted from db.'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.find_all()]}