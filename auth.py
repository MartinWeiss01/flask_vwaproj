from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from functools import wraps

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        print(session)
        if "authenticated" not in session:
            flash("You must be logged in to access this page")
            return redirect(url_for("auth.sign_in"))
        return func(*args, **kwargs)
    return decorated_function


def roles_required(*roles):
    def roles_decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if session['role'] not in roles:
                flash('You do not have permission to access this page')
                return redirect(url_for('homepage.index'))
            return func(*args, **kwargs)
        return decorated_function
    return roles_decorator