from flask_wtf import Form
from wtforms import StringField,IntegerField,TextAreaField,SubmitField,RadioField
from wtforms import ValidationError,validators

class StudentForm(Form):
    id=IntegerField(label='ID',validators=[validators.DataRequired()])
    name=StringField(label='Name',validators=[validators.DataRequired()])
    age=IntegerField(label='Age')
    gender=RadioField(label='Gender',choices=['Male','Female'])
    city=TextAreaField(label='City',validators=[validators.DataRequired()])
    submit=SubmitField('Submit')
