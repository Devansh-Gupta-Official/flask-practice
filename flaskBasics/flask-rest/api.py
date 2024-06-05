from flask import Flask, jsonify, request
from flask_restful import Api, Resource #Resource is a class that is used to define the resources that will be used in the API. #Api is a class that is used to wrap the Flask application and simplify the API creation process.

app=Flask(__name__)

api=Api(app)

class HelloWorld(Resource):
    def get(self): #GET method
        return jsonify({'hello':'world'})

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)