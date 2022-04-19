from flask import Flask
from flask_restful import Api
from route.books import BookRoute,BookRouteList

app=Flask(__name__)
api=Api()

app.config['SECRET_KEY']='restapi'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3305/sam_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(BookRoute,"/books","/books/<string:name>","/books/<int:id>")
api.add_resource(BookRouteList,"/books/")

if __name__=='__main__':
    from books_restapi.database import db
    db.init_app(app)
    api.init_app(app)
    app.run(debug=True)