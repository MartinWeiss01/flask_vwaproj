from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import forms
from service.materials_service import MaterialsService

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/materials/manage', methods=['GET', 'POST'])
def admin_update_prices():
  prices = MaterialsService.get_current_prices()
  return render_template('admin/materials/manage.html', prices=prices)

@admin_bp.route('/materials/new', methods=['GET', 'POST'])
def admin_new_material():
  form = forms.NewMaterialForm(request.form)
  if request.method == 'POST' and form.validate():
      insertedId = MaterialsService.add_new_material(name=request.form['name'], price=request.form['price'])
      if insertedId != -1:
          return redirect(url_for('admin.admin_update_prices'))
      else:
          flash('Material with this name already exists')
  return render_template('admin/materials/new.html', form=form)