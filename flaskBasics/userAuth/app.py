from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required #user has to be logged in to see this view
def welcome_user():
    return render_template('welcome_user.html')    

@app.route('/logout')
@login_required #user has to be logged in to see this view
def logout():
    logout_user() #logout the user using flask_login imports
    flash("You logged out!")
    return redirect(url_for('home'))
