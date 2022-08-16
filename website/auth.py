from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and password:
            if check_password_hash(user.password, password):
                flash('Inicio de sesion exitoso!', category='sucess')
                login_user(user, remember=True)
                return redirect(url_for('views.catalogo'))
            else:
                flash('Contraseña incorrecta, intentalo de nuevo', category='error')
        else:
            flash('El usuario no existe', category='error')

    return render_template('login.html', user=current_user)



@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters',
                  category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 characters',
                  category='error')
        elif password1 != password2:
            flash('Password dont match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            password=generate_password_hash(password1,
                                                            method='sha256'))

            db.session.add(new_user)

            db.session.commit()
            flash('Account created!', category='success')

            return redirect(url_for('views.catalogo'))

    return render_template("signup.html", user=current_user)


@auth.route('/logout')
def logout():
    flash('Sesion cerrada satisfactoriamente', category='success')
    logout_user()
    return redirect(url_for('auth.login'))
