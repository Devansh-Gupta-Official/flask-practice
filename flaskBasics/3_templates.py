from flask import Flask, render_template

app = Flask(__name__)

#inserting variable to html template using jinja
@app.route("/")
def index():
    name = "Devansh"
    letters=list(name)
    name_dict={'name':'Devansh'}
    return render_template('basic_templates.html', name=name,letters=letters,name_dict=name_dict)   

if __name__=="__main__":
    app.run(debug=True)