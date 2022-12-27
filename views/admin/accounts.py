from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
from service.user_service import UserService

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/manage', methods=['GET', 'POST'])
@auth.login_required
@auth.roles_required('admin')
def manage_accounts():
  users = UserService.get_users()
  return render_template('admin/accounts/manage.html', users=users)