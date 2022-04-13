from flask import render_template,request
from config import db
from config import app
from models import Employee

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/employee/add',methods=['POST','GET'])
def add():
    message=''
    if request.method=='POST':
        formdata=request.form
        employee=Employee.query.filter_by(eid=formdata.get('eid')).first()

        if employee:
            employee.ename=request.form['ename']
            employee.esalary=request.form['esalary']
            employee.eage=request.form['eage']
            employee.ecity=request.form['ecity']

            db.session.commit()
            message='Employee Record updated successfully'
        else:
            try:
                employees=Employee(eid=formdata.get('eid'),
                                   ename=formdata.get('ename'),
                                   esalary=formdata.get('esalary'),
                                   eage=formdata.get('eage'),
                                   ecity=formdata.get('ecity'))
                db.session.add(employees)
                db.session.commit()
                message="Employee added successfully"
            except BaseException as e:
                message=e.args[1]


    dummy = Employee(eid=0, ename="", esalary=0.0, eage=0, ecity="")
    return render_template('add.html', result=message, employee=dummy)

@app.route('/employee/display',methods=['GET'])
def display_employee_info():
    employees=Employee.query.all()
    return render_template('display.html',employees=employees)

@app.route('/employee/edit/<int:eid>',methods=['GET','post'])
def update(eid):
    employee=Employee.query.filter_by(eid=eid).first()
    if employee:
            return render_template('add.html',employee=employee)

@app.route('/employee/delete/<int:eid>',methods=['get','post'])
def delete(eid):
    employee=Employee.query.filter_by(eid=eid).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
    employees=Employee.query.all()
    return render_template('display.html',employees=employees)

@app.route('/employee/search/<int:eid>',methods=['get','post'])
def employee_search(eid):
    employee=Employee.query.filter_by(eid=eid).first()

    render_template('display.html',employees=employee)

if __name__=='__main__':
    app.run(debug=True)