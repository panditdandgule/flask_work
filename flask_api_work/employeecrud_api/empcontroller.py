from config import app
from flask import json, request
from models import Employee, db


@app.route('/employee/api/v1/', methods=['POST'])
def add_employee():
    req_data = request.get_json()
    if req_data:
        try:
            employee = Employee(name=req_data.get('name'),
                                age=req_data.get('age'),
                                salary=req_data.get('salary'))
            db.session.add(employee)
            db.session.commit()
            return json.dumps({"Success": "Data Added successfully"})
        except Exception as e:
            print(e.args)
    else:
        return json.dumps({"Error": "Something went wrong while adding data.."})


@app.route('/employee/api/v1/<int:eid>', methods=['GET'])
def search_employee(eid):
    employee = Employee.query.filter_by(id=eid).first()
    if employee:
        employee_info = {"Id": employee.id,
                         "Name": employee.name,
                         "Age": employee.age,
                         "Salary": employee.salary}
        return json.dumps({"Success": employee_info})
    else:
        return json.dumps({"Error": "Provided id is not available in database..!"})


@app.route('/employee/api/v1/', methods=['GET'])
def display_all_employee():
    all_employee = Employee.query.all()
    if all_employee:
        employee_json = []
        for employee in all_employee:
            employees = {"Id": employee.id,
                         "Name": employee.name,
                         "Age": employee.age,
                         "Salary": employee.salary}
            employee_json.append(employees)
            print()
        return json.dumps({"success": employee_json})
    else:
        return json.dumps({"Error": "Employee records are not available"})


@app.route('/employee/api/v1/<int:eid>', methods=['PUT'])
def update_employee_info(eid):
    req_data = request.get_json()
    if req_data:
        employee = Employee.query.filter_by(id=eid).first()
        if employee:
            employee.name = req_data.get("name")
            employee.age = req_data.get("age")
            employee.salary = req_data.get("salary")
            db.session.commit()
            employees = {"Id": employee.id,
                         "Name": employee.name,
                         "Age": employee.age,
                         "Salary": employee.salary}
            return json.dumps({"Success": employees})
        else:
            return json.dumps({"Error": "Employee id is not present in database..!"})
    else:
        return json.dumps({"Error": "Invalid id provided"})

@app.route('/employee/api/v1/<int:eid>',methods=['DELETE'])
def delete_employee_info(eid):
    employee=Employee.query.filter_by(id=eid).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return json.dumps({"Success":"Record Deleted successfully"})
    else:
        return json.dumps({"Error":"Provided Employee id is not present in the database"})

if __name__ == '__main__':
    app.run(debug=True)
