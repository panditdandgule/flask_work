import pymysql
from app import app
from models import Employee
from dbconfig import db
from flask import jsonify
from flask import flash,request

@app.route('/addemployee',methods=['POST'])
def post():
    try:
        json=request.json

        if request.method=='POST':
            id=json['id']
            name=json['name']
            email=json['email']
            salary=json['salary']

            employee=Employee(id=id,
                              name=name,
                              email=email,
                              salary=salary)
            db.session.add(employee)
            db.session.commit()
            resp=jsonify("Employee Added successfully")
            return resp
    except Exception as e:
        print(e)

@app.route('/employeelist')
def get():
    employees=Employee.query.all()

    return {"Employee":list(x.json for x in employees)}

if __name__=='__main__':
    app.run()