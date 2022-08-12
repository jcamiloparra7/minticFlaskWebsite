from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Cart, Product

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def catalogo():

    if request.method == 'POST':
        if current_user.is_authenticated:
            product_id = request.form.get('product_id')
            item_carrito = Cart(id_user=current_user.get_id(), id_product=product_id)
            db.session.add(item_carrito)
            db.session.commit()
            flash('Objeto añadido al carrito', category='success')
        else:
            flash('Por favor inicia sesion')
            return redirect(url_for('auth.login'))

        # if current_user.is_authenticated:
        #     redirect(url_for('views.carrito'))
        # else:
        #     redirect(url_for('auth.login'))
        #     flash('Antes de comprar debes iniciar sesion', category='info')

    inventory = Product.query.all()

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

