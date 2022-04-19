from flask_restful import Resource
from books_restapi.models.book import BookModel
from flask import request, jsonify, make_response


class BookRoute(Resource):
    def post(self):
        data = request.get_json()
        print("post data",data)
        name = data['name']
        price = data['price']
        publication = data['publication']

        obj = BookModel.find_by_name(name)
        if obj is not None:
            return make_response(jsonify({
                "message": "Book Exists", "status": 404
            }), 404)

        bookObj = BookModel(name=name, price=price, publication=publication)

        bookObj.add_to_db()

        return make_response(jsonify({
            "message": "Book Added",
            "status": 200
        }), 200)

    def get(self,name):
        # data = request.get_json()
        # print("get data",data)
        # name = data['name']


        obj = BookModel.find_by_name(name)

        if obj is not None:
            return make_response(jsonify({
                "Name": obj.name,
                "Price": obj.price,
                "Publication": obj.publication
            }), 200)

        return make_response(jsonify({
            "message": "Book Does not exists",
            "status": 404
        }), 404)

    def delete(self,name):
        # data = request.get_json()
        # name = data['name']

        obj = BookModel.find_by_name(name)

        if obj is None:
            return make_response(jsonify({
                "message": "Book Does not Exist",
                "status": 404
            }), 404)

        obj.delete_from_db()

        return make_response(jsonify({
            "message": "Book Deleted successfully",
            "status": 202
        }), 202)

    def put(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        publication = data['publication']

        obj = BookModel.find_by_name(name)

        if obj is None:
            return make_response(jsonify({
                "message": "Book does not exists",
                "status": 404
            }), 404)

        if price:
            obj.price = price
        if publication:
            obj.publication = publication
        obj.add_to_db()

        return make_response(jsonify({
            "message": "Book Details Updated",
            "status": 200
        }), 200)

class BookRouteList(Resource):
    def get(self):
        books=BookModel.query.all()
        if books:
            bookslist=[]
            for book in books:
                bookslst={"ID:":book.id,
                          "Name:":book.name,
                          "Price:":book.price,
                          "Publication:":book.publication}
                bookslist.append(bookslst)
            return jsonify({"success":bookslist})
        else:
            return jsonify({"Error":"Booklist is empty"})
