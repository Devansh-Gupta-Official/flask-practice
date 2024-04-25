from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY']="secretkey"

class InfoForm(FlaskForm):
    breed=StringField("What breed are you?",validators=[DataRequired()])
    neutered=BooleanField("Have you been neutered?")
    mood=RadioField("Please choose your mood!", choices=[('mood_one','Happy'),('mood_two','Sad')])
    food_choice = SelectField(u"Pick your favourite food:",choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    feedback=TextAreaField()
    submit=SubmitField('Submit')


@app.route('/',methods=['POST','GET'])
def index():
    form = InfoForm()
    #passing data got from form to session and then to another template
    if form.validate_on_submit():
        session['breed']=form.breed.data
        session['neutered']=form.neutered.data
        session['mood']=form.mood.data
        session['food']=form.food_choice.data
        session['feedback']=form.feedback.data

        return redirect(url_for('thankyou'))
        
    return render_template('7_index.html',form=form)   #rendering of home page

@app.route('/thankyou')
def thankyou():
    return render_template('7_thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)