from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import auth
from views.admin.materials import materials_bp

admin_bp = Blueprint('admin', __name__)
admin_bp.register_blueprint(materials_bp, url_prefix='/materials')

@admin_bp.route('/')
@auth.login_required
@auth.roles_required('admin')
def index():
  return render_template('homepage/index.html')
