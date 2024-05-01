import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager=LoginManager()

app=Flask(__name__)

app.config['SECRET_KEY']='mysecret'
basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)
app.app_context().push()

login_manager.init_app(app) #configure login in app
login_manager.login_view='login' #redirect to login page if not logged in