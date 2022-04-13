from flask_wtf import Form  # import parent class Form
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, RadioField, \
    SubmitField  # imported all fields to form button
from wtforms.validators import ValidationError, DataRequired


class GogetRegistrationForm(Form):  # imported parent class Form
    name = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    phoneNumber = IntegerField(label='Enter Mobile Number', validators=[DataRequired()])
    gender = RadioField(label='Gender', choices=['Male', 'Female'])
    address = TextAreaField(label='Address')
    age = IntegerField(label='Age')
    submit = SubmitField("Submit")
