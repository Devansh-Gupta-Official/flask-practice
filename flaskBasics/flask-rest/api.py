from flask import Flask, jsonify, request
from flask_restful import Api, Resource #Resource is a class that is used to define the resources that will be used in the API. #Api is a class that is used to wrap the Flask application and simplify the API creation process.
from secure_check import authenticate,identity #importing the authenticate and identity functions from the secure_check.py file
# from flask_jwt import JWT,jwt_required #importing the JWT class from the flask_jwt module

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app=Flask(__name__)
app.config['SECRET KEY']='mysecret' #secret key for the JWT token
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db)
app.app_context().push()

api=Api(app)
# jwt=JWT(app,authenticate,identity) #JWT class takes 3 arguments: the Flask app, the authenticate function and the identity function

# class HelloWorld(Resource):  
#     def get(self): #GET method
#         return jsonify({'hello':'world'})


class Puppy(db.Model):
    name=db.Column(db.String(80),primary_key=True)
    def __init__(self,name):
        self.name=name
    def json(self):
        return {'name':self.name}



# {'name':'Rufus'},{'name':'Fido'},{'name':'Spike'},.....
puppies=[]
class PuppyNames(Resource):
    def get(self,name):
        # for pup in puppies:
        #     if pup['name']==name:
        #         return pup
        pup=Puppy.query.filter_by(name=name).first() #crud with database
        if pup:
            return pup.json()
        else:
            return {'name':None},404   #404 is the status code for not found and it is returned when the name is not found in the list of puppies
    
    def post(self,name):
        # pup={'name':name}
        # puppies.append(pup)
        pup=Puppy(name=name)
        db.session.add(pup)
        db.session.commit()
        return pup.json()

    def delete(self,name):
        # for ind,pup in enumerate(puppies):
        #     if pup['name']==name:
        #         deleted_pup=puppies.pop(ind)
        #         return {'note':'delete success'}
        pup=Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note':'delete success'}

class AllNames(Resource):
    # @jwt_required() #this decorator is used to protect the route and requires a valid JWT token to access the route
    def get(self):
        # return {'puppies':puppies}
        puppies=Puppy.query.all()
        return [pup.json() for pup in puppies]

api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)