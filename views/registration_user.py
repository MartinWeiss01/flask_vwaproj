from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from service.user_service import UserService
import forms


registration_bp = Blueprint('reg', __name__)



@registration_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form= forms.RegistrationUserForm(request.form)
    if request.method == 'POST':
        UserService.registration_user(



        )
        flash('Registration is done')
        return redirect(url_for('auth_bp.sign_in'))
    return render_template('registration/registration.html', form=form)