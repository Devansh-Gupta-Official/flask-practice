from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class Addform(FlaskForm):
    name=StringField("Name the Puppy!!")
    submit=SubmitField("Submit")

class DelForm(FlaskForm):
    id=IntegerField('ID number of puppy to remove.')
    submit=SubmitField("Remove Puppy")

