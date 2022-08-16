from website import create_app
from website import db
from website.models import CartItems, User, Product

app = create_app()

def createUser():
    """
    id
    name
    """
    for i in range(10):
        createUser = User(id=i, name=f"xhlar{i}")
        db.session.add(createUser)
        db.session.commit()

def createProducts():
    """
    id
    name
    description
    price
    """
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

    for i in range(1, 11):
        createRelation = CartItems(user_id=i, product_id=i, quantity=1, date="NULL")
        db.session.add(createRelation)
        db.session.commit()

createUser()
createProducts()
createRelationProduct()
