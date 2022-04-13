from config import app
from config import db
from models import Employee,Address
from forms import Employee,Address,DelForm
from flask import render_template,redirect,url_for



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_employee',methods=['GET','POST'])
def add_employee():
    form=Employee()
    if form.validate_on_submit():
        name=form.name.data
        age=form.age.data

        employees=Employee(name,age)
        db.session.add(employees)
        db.session.commit()
        return redirect(url_for('list_employee'))
    return render_template('add.html',form=form)

@app.route('/add_address', methods=['POST', 'GET'])
def add_address():
    form = Address()
    if form.validate_on_submit():
        city = form.city.data
        country=form.country.data
        emp_id = form.emp_id.data

        new_addr = Address(city,
                            country,
                             emp_id)
        db.session.add(new_addr)
        db.session.commit()

        return redirect(url_for('list_employee'))
    return render_template('address.html', form=form)


@app.route('/list_employee')
def list_employee():
    employees=Employee.query.all()
    return render_template('list_employee.html',employees=employees)

@app.route('/delete', methods=['GET', 'POST'])
def del_employee():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for('list_employee'))

    return render_template('delete.html', form=form)


if __name__=='__main__':
    app.run(debug=True,port=5000)