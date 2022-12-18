from flask import Flask, render_template, request, flash, redirect, url_for, session
from views.auth import auth_bp
from views.homepage import homepage
from database import database
from views.registration_user import registration_bp
import forms

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
database.init_app(app)

app.register_blueprint(homepage, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(registration_bp, url_prefix='/')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)


