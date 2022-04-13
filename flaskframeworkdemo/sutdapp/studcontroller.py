from config import app
from config import db
from flask import request,render_template
from models import StudentModel

@app.route('/')
@app.route('/student')
def home():
    return render_template('index.html',flag=False)

@app.route('/student/add',methods=['POST','GET'])
def student_add_info():
    message=''
    if request.method=='POST':
        formdata=request.form

        student=StudentModel.query.filter_by(sid=formdata.get('sid')).first()

        if student:
            student.sid=formdata.get('sid')
            student.sname=formdata.get('sname')
            student.sage=formdata.get('sage')
            student.scity=formdata.get('scity')
            db.session.commit()
            message='Updated Stud info successfully'

        else:
            try:
                students=StudentModel(sid=formdata.get('sid'),
                                      sname=formdata.get('sname'),
                                      sage=formdata.get('sage'),
                                      scity=formdata.get('scity'))

                db.session.add(students)
                db.session.commit()
                message="Student info added successfully"
            except BaseException as e:
                message=e.args[1]
    dummy=StudentModel(sid=0,sname='',sage=0,scity='')
    return render_template('add.html',result=message,students=dummy)

@app.route('/student/display',methods=['GET'])
def display_student_info():
    students=StudentModel.query.all()
    return render_template('display.html',students=students)

@app.route('/student/edit/<int:sid>',methods=['GET','POST'])
def update_student_info(sid):
    students=StudentModel.query.filter_by(sid=sid).first()
    if students:
        return render_template('add.html',students=students)

@app.route('/student/search/<int:sid>',methods=['get'])
def search_student():
    students = None
    if request.method == 'POST':
        user_selection = request.form.get('search')
        user_input = request.form.get('inputval')
    if user_selection == 'ID':
        students = StudentModel.query.filter_by(sid=user_input).first()
    elif user_selection == 'NAME':
        students = StudentModel.query.filter(StudentModel.sname == user_input).all()

    return render_template('index.html', flag=True, students=students)

@app.route('/student/delete/<int:sid>',methods=['GET','POST'])
def delete_studetn_info(sid):
    students=StudentModel.query.filter_by(sid=sid).first()
    if students:
        db.session.delete(students)
        db.session.commit()
    students=StudentModel.query.all()
    return render_template('display.html',students=students)


if __name__=='__main__':
    app.run(debug=True)