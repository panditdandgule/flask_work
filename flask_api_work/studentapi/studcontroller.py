import bdb

from config import app, api
from flask_restful import Resource, reqparse, request
from models import StudentModel, db


class StudentModelView(Resource):
    def get(self):
        students = StudentModel.query.all()
        return {'Students': list(x.json() for x in students)}

    def post(self):
        data = request.get_json()
        new_student = StudentModel(data['name'], data['age'])
        db.session.add(new_student)
        db.session.commit()
        db.session.flush()

        return new_student.json(), 201


class SingleStudentView(Resource):
    def get(self, id):
        student = StudentModel.query.filter_by(id=id).first()
        if student:
            return student.json()
        else:
            return {'message': "student id not found"}, 404

    def put(self, id):
        data = request.get_json()
        student = StudentModel.query.filter_by(id=id).first()
        if student:
            student.name = data['name']
            student.price = data['age']

        else:
            student = StudentModel(id=id, **data)

        db.session.add(student)
        db.session.commit()

        return student.json()

    def delete(self, id):
        student = StudentModel.query.filter_by(id=id).first()
        if student:
            db.session.delete(student)
            db.session.commit()
            return {'message': 'Deleted sucessfully'}
        else:
            return {'message': "student id not found"}, 404


api.add_resource(StudentModelView, '/student')
api.add_resource(SingleStudentView, '/student/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
