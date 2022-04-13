from flask_wtf import Form
from wtforms import StringField
from wtforms import TextAreaField,IntegerField,SubmitField,RadioField,SelectField
from wtforms import ValidationError,validators

class ContactForm(Form):
    name=StringField("Candidate Name",[validators.DataRequired("Please enter your name")])
    Gender=RadioField('Gender',choices=[('M','Male'),('F','Female')])
    Address=TextAreaField('Address')

    email=StringField("Email",[validators.DataRequired("Please enter your email address")])

    Email=IntegerField("Age")
    language=SelectField("Programming Languages", choices = [('java', 'Java'),('py', 'Python')])

    submit=SubmitField("Submit")
