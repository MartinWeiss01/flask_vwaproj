from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
import forms
from service.user_service import UserService

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signin', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignInForm(request.form)
    if request.method == 'POST':
        user = UserService.verify(login=request.form['login'], password=request.form['password'])
        if not user:
            flash('Incorrect login or password')
        else:
            session['authenticated'] = 1
            session['login'] = user['login']
            session['role'] = user['role']
            return redirect(url_for('homepage.index'))
    return render_template("auth/sign_in.html", form=form)


@auth_bp.route('/signout')
@auth.login_required
def signout():
    session.pop("authenticated")
    session.pop("login")
    session.pop("role")
    return redirect(url_for('homepage.index'))
