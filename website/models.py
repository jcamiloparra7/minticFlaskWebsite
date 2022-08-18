from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column
import uuid
from strenum import StrEnum
from enum import auto
from website import db

# users_products = db.Table('users_products',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
#     db.Column('quantity', db.Integer),
#     db.Column('date', db.DateTime(timezone=True), default=func.now())
#     )

# class CartItems(db.Model):
#     __tablename__ = "car_items"
#     user_id = Column(ForeignKey("users.id"), primary_key=True)
#     product_id = Column(ForeignKey("products.id"), primary_key=True)
#     quantity = Column(String(50))
#     date = Column(String(50))
#     # item = relationship("Product")

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Integer)
    price = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(200))
    users = relationship(
        "Cart",
        back_populates="product"
    )



class User(db.Model, UserMixin):
    class ROLES(StrEnum):
        SUPERADMIN = auto()
        ADMIN = auto()
        USUARIO = auto()

    __tablename__ = "user"
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150), unique=True)
    last_name = db.Column(db.String(150), unique=True)
    rol = db.Column(db.String(20), default=ROLES.USUARIO.value)
    # cart = relationship("CartItems")
    products = relationship(
        "Cart",
        back_populates="user"
    )

# class Product(db.Model):
#     __tablename__ = 'product'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     description = db.Column(db.String(1000))
#     price = db.Column(db.Integer)
#     image_url = db.Column(db.String(200))
#     user = relationship("Cart", back_populates="product")
#     # cart = db.relationship('Cart', backref="productocarrito")

# class User(db.Model, UserMixin):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     password = db.Column(db.String(150))
#     email = db.Column(db.String(150), unique=True)
#     first_name = db.Column(db.String(150), unique=True)
#     last_name = db.Column(db.String(150), unique=True)

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'), primary_key=True)
    user_id = Column(ForeignKey('user.id'), primary_key=True)
    quantity= db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    product = relationship("Product", back_populates="users")
    user = relationship("User", back_populates="products")



# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
#     id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
    # cart = db.relationship('Cart')


# class Cart(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # id_product = db.Column(db.Integer, db.ForeignKey('product.id'))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
