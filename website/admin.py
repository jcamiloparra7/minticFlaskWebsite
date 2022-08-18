from flask import Blueprint
from flask_login import login_required
from flask import render_template

admin = Blueprint('admin', __name__)

@admin.route('/')
@login_required
def opciones_admin():
    return render_template('admin.html')

@admin.route('/gestion_usuarios')
@login_required
def eliminar_usuario():
    return render_template('admin.html')

@admin.route('/gestion_usuarios/<id_usuario>')
@login_required
def editar_usuario(id_usuario):
    return render_template('admin.html')