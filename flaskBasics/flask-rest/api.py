from flask import Flask, jsonify, request
from flask_restful import Api, Resource #Resource is a class that is used to define the resources that will be used in the API. #Api is a class that is used to wrap the Flask application and simplify the API creation process.
from secure_check import authenticate,identity #importing the authenticate and identity functions from the secure_check.py file
from flask_jwt import JWT,jwt_required #importing the JWT class from the flask_jwt module


app=Flask(__name__)
app.config['SECRET KEY']='mysecret' #secret key for the JWT token
api=Api(app)
jwt=JWT(app,authenticate,identity) #JWT class takes 3 arguments: the Flask app, the authenticate function and the identity function

# class HelloWorld(Resource):  
#     def get(self): #GET method
#         return jsonify({'hello':'world'})


# {'name':'Rufus'},{'name':'Fido'},{'name':'Spike'},.....
puppies=[]
class PuppyNames(Resource):
    def get(self,name):
        for pup in puppies:
            if pup['name']==name:
                return pup
        return {'name':None},404   #404 is the status code for not found and it is returned when the name is not found in the list of puppies
    
    def post(self,name):
        pup={'name':name}
        puppies.append(pup)
        return pup

    def delete(self,name):
        for ind,pup in enumerate(puppies):
            if pup['name']==name:
                deleted_pup=puppies.pop(ind)
                return {'note':'delete success'}

class AllNames(Resource):
    @jwt_required() #this decorator is used to protect the route and requires a valid JWT token to access the route
    def get(self):
        return {'puppies':puppies}

api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)