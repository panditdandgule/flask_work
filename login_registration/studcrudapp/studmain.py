from config import app
from models import StudentModel, Users, db
from flask import request, render_template, redirect, abort, session, url_for


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home')
def home():
    counts = StudentModel.query.count()
    students = StudentModel.query.all()
    if 'email' in session:
        return render_template('home.html', students=students, counts=counts)
    else:
        return redirect('/')


@app.route('/loginvalidation', methods=['POST', 'GET'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    users = Users.query.filter(Users.email == email, Users.password == password).first()

    if users:
        session['email'] = users.email
        #if users.check_password(request.form.get('password')):
        return redirect(url_for('home'))
    else:
        return redirect('/')


@app.route('/adduser', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('names')
        email = request.form.get('emails')
        password = request.form.get('passwords')

        users = Users(name=name,
                      email=email,
                      password=password
                      )
        #users.set_password(password=password)
        db.session.add(users)
        db.session.commit()
        msg = 'User {} registered successfully'.format(users.email)

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('email')
    return redirect('/')


@app.route('/addstudent', methods=['POST', 'GET'])
def add_studentinfo():
    if request.method == 'GET':
        return render_template('create.html')

    if request.method == 'POST':
        hobby = request.form.getlist('hobbies')
        hobbies = ','.join(hobby)
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        email = request.form.get('email')
        password = request.form.get('password')
        hobbies = hobbies
        country = request.form.get('country')

        students = StudentModel(firstname=fname,
                                lastname=lname,
                                age=age,
                                gender=gender,
                                email=email,
                                password=password,
                                hobbies=hobbies,
                                country=country)
        db.session.add(students)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/display', methods=['GET'])
def display_studentinfo():
    students = StudentModel.query.all()
    return render_template('index.html', students=students)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update_studentinfo(id):
    student = StudentModel.query.filter_by(id=id).first()
    if student:
        db.session.delete(student)
        db.session.commit()

        hobby = request.form.getlist('hobbies')
        hobbies = ','.join(hobby)
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        email = request.form.get('email')
        password = request.form.get('password')
        hobbies = hobbies
        country = request.form.get('country')

        students = StudentModel(firstname=fname,
                                lastname=lname,
                                age=age,
                                gender=gender,
                                email=email,
                                password=password,
                                hobbies=hobbies,
                                country=country)
        db.session.add(students)
        db.session.commit()
        return redirect('/display')
        #return redirect('/display')
    #return f"student with id={id} does not exist"

    return render_template('update.html', student=student)


@app.route('/delete/<int:id>')
def remove_student(id):
    student = StudentModel.query.filter_by(id=id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('home'))
    abort(404)

    return render_template('delete.html', student=student)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
