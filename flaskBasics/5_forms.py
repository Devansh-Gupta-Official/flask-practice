from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('5_index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('5_signup.html')

@app.route('/thankyou')
def thank_you():
    first=request.args.get('first')
    last=request.args.get('last')
    return render_template('5_thankyou.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('5_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)