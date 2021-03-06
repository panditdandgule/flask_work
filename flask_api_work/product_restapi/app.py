import os
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.store import Store, StoreList
#from resources.user import UserRegister
from security import authenticate, identity

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sam_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS']=True
app.secret_key='fjsdlkfjdslfkdjwkjfls'
api=Api(app)

jwt=JWT(app,authenticate,identity)

# api.add_resource(UserRegister, '/register') # registration of new users disabled on production
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    # importing here to avoid circular imports
    from product_restapi.db import db

    db.init_app(app)
    app.run(port=5000, debug=False)