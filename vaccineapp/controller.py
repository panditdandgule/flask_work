from config import app
from models import Doctor,Patient,VaccineDose
from flask import render_template, request, redirect, url_for
from config import db


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/registerdoctor',methods=['POST'])
def register_doctor():
    form=request.form
    doctor=Doctor(name=request.form['name'],
                  email=request.form['email'],
                  phone=request.form['phone'],
                  govid=request.form['govid'],
                  )
    doctor.set_password(form['password'])
    db.session.add(doctor)
    db.session.commit()
    return "Successfully Registration Completed"

@app.route('/logindoctor',methods=['post'])
def login_doctor():
    form=request.form
    doctor=Doctor.query.filter_by(email=form['email']).first()
    if doctor.check_password(form['password']):
        return redirect(url_for('patients'))
    else:
        return 'Error'

@app.route('/patients',methods=['post','get'])
def patients():
    return "Successfully Logged in"


@app.route('/patient')
def individual_patient():
    return "Individual patient"

@app.route('/list_patients',methods=['get'])
def list_patients():
    email_address=request.form['email']
    return "Email address sucessfully submitted"


if __name__=='__main__':
    app.run(debug=True,port=5000)