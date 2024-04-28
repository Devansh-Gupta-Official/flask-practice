import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#using flask migrate
from flask_migrate import Migrate

#setting up sqllite database
basedir=os.path.abspath(os.path.dirname(__file__))   #getting the current directory
#__file__ -> C://Users/.../flaskBasics/9_basic_sql.py

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

Migrate(app,db)  #connects application with database so that changes in table are propogated

#setup context **IMPORTANT**
app.app_context().push()


#creating a model
class Puppy(db.Model):

    __tablename__ = 'puppies'   #overriding default tablename

    #creating columns for table
    id = db.Column(db.Integer, primary_key=True)   #primary key 
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    breed=db.Column(db.Text)

    #setup init method for class
    def __init__(self, name, age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):   #gives string representation of object
        return f"Puppy {self.name} is {self.age} year/s old."




