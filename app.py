from flask import Flask, render_template, request, flash, redirect, url_for, session

import auth

from database import database

import forms

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
database.init_app(app)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')