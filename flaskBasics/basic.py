from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<hi>Welcome to my first web page!</h1>"

if __name__=="__main__":
    app.run()