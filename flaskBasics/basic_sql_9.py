import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#setting up sqllite database
basedir=os.path.abspath(os.path.dirname(__file__))   #getting the current directory
#__file__ -> C://Users/.../flaskBasics/9_basic_sql.py

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

#setup context **IMPORTANT**
app.app_context().push()


#creating a model
class Puppy(db.Model):

    __tablename__ = 'puppies'   #overriding default tablename

    #creating columns for table
    id = db.Column(db.Integer, primary_key=True)   #primary key 
    name=db.Column(db.Text)
    age=db.Column(db.Integer)

    #setup init method for class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):   #gives string representation of object
        return f"Puppy {self.name} is {self.age} year/s old."




