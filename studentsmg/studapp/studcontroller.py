from flask import render_template, url_for, redirect
from models import Student, Father
from forms import AddForm, DelForm, AddFatherForm
from student import app
from student import db

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_father', methods=['POST', 'GET'])
def add_father():
    form = AddFatherForm()
    if form.validate_on_submit():
        name = form.name.data
        stud_id = form.stud_id.data

        new_father = Father(name,
                            stud_id)
        db.session.add(new_father)
        db.session.commit()

        return redirect(url_for('list_student'))
    return render_template('add_father.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data

        new_student = Student(name)

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('list_student'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_student():
    students = Student.query.all()
    return render_template('list.html', students=students)


@app.route('/delete', methods=['GET', 'POST'])
def del_student():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('list_student'))

    return render_template('delete.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
