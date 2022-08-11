from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def catalogo():
    if request.method == 'POST':
        pass

    inventario = [{'name': 'Hamburguesa',
                  'price': 10000},
                  {'name': 'Perro',
                   'price': 8000}]

    return render_template("catalogo.html", inventario=inventario)

@views.route('/carrito', methods=['GET', 'POST'])
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

