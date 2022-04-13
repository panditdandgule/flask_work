from flask import Flask, request, render_template, abort, redirect
from models import EmployeeModel, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        city = request.form['city']

        employee = EmployeeModel(
            fname=fname,
            lname=lname,
            age=age,
            city=city
        )
        db.session.add(employee)
        db.session.commit()
        return redirect('/')


@app.route('/', methods=['GET'])
def retrivelist():
    employees = EmployeeModel.query.all()
    return render_template('index.html', employees=employees)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    employees = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        db.session.delete(employees)
        db.session.commit()
        if employees:
            fname = request.form['fname']
            lname = request.form['lname']
            age = request.form['age']
            city = request.form['city']

            employees = EmployeeModel(
                fname=fname,
                lname=lname,
                age=age,
                city=city

            )
            db.session.add(employees)
            db.session.commit()
            return redirect('/')

        return f"Employee id with {id} does not exists"
    return render_template('update.html')


@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/')
        abort(404)
    return render_template('delete.html')
