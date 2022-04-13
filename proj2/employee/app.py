from flask import Flask, render_template, redirect, request,abort
from models import EmployeeModel, db
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3305/proj2db'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_PORT']=3305
# app.config['MYSQL_DB'] = 'proj2db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('/create.html')

    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        country = request.form['country']

        employee = EmployeeModel(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            gender=gender,
            country=country
        )
        db.session.add(employee)
        db.session.commit()
        return redirect('/')


@app.route('/', methods=['GET'])
def retrivelist():
    employee = EmployeeModel.query.all()
    return render_template('index.html', employee=employee)

@app.route('/<int:id>/edit',methods=['GET','POST'])
def update(id):
    employees=EmployeeModel.query.filter_by(id=id).first()

    if request.method=='POST':
        db.session.delete(employees)
        db.session.commit()
        if employees:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            country = request.form['country']

            employee = EmployeeModel(
                firstname=firstname,
                lastname=lastname,
                email=email,
                password=password,
                gender=gender,
                country=country
            )
            db.session.add(employee)
            db.session.commit()
            return redirect('/')
        return f'employee with id={id} does not exists'
    return render_template('update.html',employees=employees)



@app.route('/<int:id>/delete',methods=['GET','POST'])
def delete(id):
    employee=EmployeeModel.query.filter_by(id=id).first()
    if request.method=='POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=True)
