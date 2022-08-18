from website import create_app
from website import db
from website.models import Cart, User, Product

app = create_app()


def createUser():
    """
    id
    name
    """
    with app.app_context():
        for i in range(10):
            createUser = User(id=i, email=f"xhlar{i}@xhlar.com")
            db.session.add(createUser)
            db.session.commit()

def createProducts():
    """
    id
    name
    description
    price
    """
    with app.app_context():
        for i in range(1, 11):
            createProduct = Product(id=i, name=f"product {i}", description=f"description{i}", price=f"{2000*i}")
            db.session.add(createProduct)
            db.session.commit()

def createRelationProduct():
    """
    user_id
    product_id
    quantity
    date
    """

    with app.app_context():
        for i in range(1, 11):
            usuario = User.query.get(i)
            producto = Product.query.get(i)
            item_carrito = Cart(id=i, product_id=i, user_id=i, quantity=1, date=None)
            # item_carrito.product = producto
            # usuario.products.append(item_carrito)
            # createRelation = Cart(user_id=i, product_id=i, quantity=1, date="NULL")
            db.session.add(item_carrito)
            db.session.commit()

createUser()
createProducts()
createRelationProduct()
