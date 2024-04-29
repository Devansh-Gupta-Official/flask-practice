from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Owner:')
    pup_id = IntegerField('Id Number of Puppy:')
    submit = SubmitField('Submit Owner')