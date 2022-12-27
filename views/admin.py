from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from service.materials_service import MaterialsService

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/materials/manage', methods=['GET', 'POST'])
def admin_update_prices():
  prices = MaterialsService.get_current_prices()
  return render_template('admin/materials/manage.html', prices=prices)
