from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<hi>Welcome to my Puppy page!</h1>"

@app.route("/puppy_latin/<name>")
def viewhuman(name):
    if name[-1]=='y':
        return name[:-1]+"iful"
    else:
        return name+"y"


if __name__=="__main__":
    app.run(debug=True)