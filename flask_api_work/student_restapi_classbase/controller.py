from flask import request, jsonify, make_response
from models import Student
from flask_restful import Resource


class StudentRoute(Resource):
    def post(self):
        req_data = request.get_json()
        name = req_data.get('name')
        age = req_data.get('age')
        city = req_data.get('city')

        obj = Student.find_by_id(req_data.get('id'))

        if obj is not None:
            return make_response(jsonify({"Error": "Id Already Exists",
                                          "status": 404}), 404)

        studobj = Student(name=name, age=age, city=city)
        studobj.add_to_db()

        return make_response(jsonify({
            "message": "Data Added Successfully",
            "status": 200,
        }), 200)

    def get(self):
        students = Student.query.all()
        if students:
            studlist = []
            for stud in students:
                student = {"Id": stud.id,
                           "Name": stud.name,
                           "Age": stud.age,
                           "City": stud.city}
                studlist.append(student)
            return make_response(jsonify({"students": studlist}))
        else:
            return make_response(jsonify({"Error": "Records are not available"}))


    # def get(self,id):
    #
    #     student = Student.find_by_id(id)
    #
    #     if student:
    #         return make_response(jsonify({"Id": student.id,
    #                                       "Name": student.name,
    #                                       "Age": student.age,
    #                                       "City": student.city}))
    #     else:
    #         return make_response(jsonify({"message": "Id not exists"}))


    def delete(self, id):
        student = Student.find_by_id(id)
        if student:
            student.delete_from_db()
            return make_response(jsonify({"message": "Id deleted successfully"}))
        else:
            return make_response(jsonify({"message": "Id is not exists"}))

    def put(self, id):
        student = Student.find_by_id(id)
        req_data = request.get_json()
        if student:
            student.name = req_data.get('name')
            student.age = req_data.get('age')
            student.city = req_data.get('city')
            student.add_to_db()
            return make_response(jsonify({"message": "Data updated successfully",
                                          "status": "success"}, 200), 200)
        else:
            return make_response(jsonify({"Error": "Id is not exists"}))
