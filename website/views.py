from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
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

    productos =  Product.query.all()
    return render_template("catalogo.html", inventario=productos)

@views.route('/carrito', methods=['GET', 'POST'])
@login_required
def carrito():
    if request.method == 'POST':
        pass

    # If user is anonymous
    if current_user.is_anonymous:
        carritoUsuario = []
    else:
        # Cart products without quantity
        carritoUsuario = current_user.products

    return render_template("cart.html", carrito=carritoUsuario)

@views.route('/carrito/<add>', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        pass



    return render_template("cart.html", inventario=inventario)

@views.route('/producto/<id>', methods = ['GET', 'POST'])
def producto(id):
    producto = Product.query.get_or_404(id)
    return render_template("product.html", producto=producto)
