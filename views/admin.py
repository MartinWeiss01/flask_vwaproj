from flask import Blueprint, render_template, session, redirect, url_for, request, flash

import forms
from service.materials_service import MaterialsService

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/materials/manage', methods=['GET', 'POST'])
def update_prices():
  prices = MaterialsService.get_current_prices()
  return render_template('admin/materials/manage.html', prices=prices)

@admin_bp.route('/materials/manage/<int:material_id>', methods=['GET', 'POST'])
def update_material(material_id):
  form = forms.MaterialForm(request.form)
  material_name = MaterialsService.get_material_name(material_id)
  if(material_name == None):
    return redirect(url_for('admin.update_prices'))
  if request.method == 'POST' and form.validate():
      if(request.form['name'] == material_name):
        if(MaterialsService.update_price(material_id=material_id, price=request.form['price'])):
          return redirect(url_for('admin.update_prices'))
        else:
          flash('An unexpected error occured')
      else:
        if(MaterialsService.update_name(material_id=material_id, name=request.form['name'])):
          if(MaterialsService.update_price(material_id=material_id, price=request.form['price'])):
            return redirect(url_for('admin.update_prices'))
          else:
            flash('An unexpected error occured')
        else:
          flash('An unexpected error occured')
  else:
    return render_template('admin/materials/update.html', form=form, material_name=material_name)

@admin_bp.route('/materials/new', methods=['GET', 'POST'])
def new_material():
  form = forms.MaterialForm(request.form)
  if request.method == 'POST' and form.validate():
      insertedId = MaterialsService.add_new_material(name=request.form['name'], price=request.form['price'])
      if insertedId != -1:
          return redirect(url_for('admin.update_prices'))
      else:
          flash('Material with this name already exists')
  return render_template('admin/materials/new.html', form=form)