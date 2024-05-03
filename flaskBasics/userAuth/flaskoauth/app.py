#also add http://localhost:5000/login/google/authorized and http://127.0.0.1:5000/login/google/authorized to the authorized redirect URIs in the google cloud console

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'   #setting environment variables as we are running oauth locally

from flask import Flask, redirect, url_for, session, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app=Flask(__name__)

google_client_id = os.environ.get('GOOGLE_CLIENT_ID')
google_client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')

app.config['SECRET_KEY'] = "mysecretkey"

blueprint=make_google_blueprint(client_id=google_client_id, client_secret=google_client_secret, offline=True, scope=['profile', 'email'])    #scope is a list we want back which is a list of profile and email

app.register_blueprint(blueprint,url_prefix='/login')   #registering the blueprint with the app


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    #return internal server error if not logged in
    resp = google.get('/oauth2/v1/userinfo')
    assert resp.ok, resp.text   #wont assert if the response is not ok
    email = resp.json()['email']
    return render_template('welcome.html',email=email)

@app.route('/login/google')
def login():
    if not google.authorized:   #google was imported from flask_dance.contrib.google
        return render_template(url_for('google.login'))   #redirecting to google login page
    
    resp = google.get('/oauth2/v1/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

if __name__ == '__main__':
    app.run()   #no debug mode


