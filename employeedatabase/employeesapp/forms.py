
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField


class Employee(FlaskForm):
    name=StringField(label='Employee Name:')
    age=IntegerField(label='Age:')
    submit=SubmitField("Submit")

class Address(FlaskForm):
    city=StringField(label='City')
    country=StringField(label='Country')
    submit=SubmitField("Add Address")

class DelForm(FlaskForm):
    id=IntegerField("Id no. of student to remove: ")
    submit=SubmitField("Remove Student: ")
