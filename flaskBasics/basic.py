from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<hi>Welcome to my first web page!</h1>"

#working with basic routing
@app.route("/information")
def info():
    return "<hi>I am new to Flask</hi>"

#dynamic routing
@app.route("/human/<name>")
def viewhuman(name):
    return "<h1>This is a page for {}</h1>".format(name.upper())

if __name__=="__main__":
    app.run()