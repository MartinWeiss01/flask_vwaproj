from flask import Flask, render_template, request, flash, redirect, url_for, session
from views.auth import auth_bp
from views.homepage import homepage
from views.admin.admin import admin_bp
from database import database
from service.materials_service import MaterialsService

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
database.init_app(app)

app.register_blueprint(homepage, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/prices')
def view_current_prices():
    prices = MaterialsService.get_current_prices()
    return render_template("prices.html", prices=prices)

@app.route('/stats')
def view_all_stats():
    stats = MaterialsService.get_stats()
    return render_template("stats.html", stats=stats)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)


