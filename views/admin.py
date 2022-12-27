from flask import Blueprint, render_template, session, redirect, url_for, request, flash

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/', methods=['GET', 'POST'])
def preview():
    return render_template('homepage/index.html')