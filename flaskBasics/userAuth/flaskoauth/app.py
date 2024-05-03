import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'   #setting environment variables as we are running oauth locally

from flask import Flask, redirect, url_for, session, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app=Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

blueprint=make_google_blueprint(client_id='', client_secret='', offline=True, scope=['profile', 'email'])    #scope is a list we want back which is a list of profile and email

app.register_blueprint(blueprint,url_prefix='/login')   #registering the blueprint with the app


@app.route('/')
def index():
    return render_template('home.html')

