from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Product

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def catalogo():
    if request.method == 'POST':
        if current_user.is_authenticated:
            pass
        else:
            redirect(url_for('auth.login'))
            flash('Antes de comprar debes iniciar sesion', category='info')

    inventory = Product.query.all()

    inventario = [{'name': 'Hamburguesa',
                  'price': 10000},
                  {'name': 'Perro',
                   'price': 8000}]

    return render_template("catalogo.html", inventario=inventory)

@views.route('/carrito', methods=['GET', 'POST'])
@login_required
def carrito():
    if request.method == 'POST':
        pass

    inventario = {'1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7
                  }

    return render_template("cart.html", inventario=inventario)

