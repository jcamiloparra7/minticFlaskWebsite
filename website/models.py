from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    image_url = db.Column(db.String(200))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150), unique=True)
    last_name = db.Column(db.String(150), unique=True)
    cart = db.relationship('Cart')


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
