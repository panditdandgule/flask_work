import datetime

from config import db
from werkzeug.security import check_password_hash, generate_password_hash


class Doctor(db.Model):
    id = db.Column('d_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(30), nullable=False)
    email = db.Column('email', db.String(30), index=True, unique=True, nullable=False)
    phone = db.Column('phone', db.String(12), unique=True, nullable=False)
    govid = db.Column('gov_id', db.String(6), unique=True, nullable=True)
    password = db.Column('password', db.String(128))
    patient = db.relationship('Patient', backref='doctor', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Patient(db.Model):
    id = db.Column('p_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(30), nullable=False)
    email = db.Column('email', db.String(30), index=True, unique=True, nullable=False)
    phone = db.Column('phone', db.String(12), unique=True, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.d_id'))
    vaccine_dose = db.relationship('VaccineDose', backref='patient')


class VaccineDose(db.Model):
    id = db.Column('v_id', db.Integer, primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    doseno = db.Column(db.Integer, nullable=False)
    doseid = db.Column(db.Integer, nullable=False)
    dosedate=db.Column(db.DateTime(timezone=True),default=datetime.datetime.now())
    patient_id=db.Column(db.Integer,db.ForeignKey('patient.p_id'))

db.create_all()