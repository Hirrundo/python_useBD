from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Product, Customer, Order

engine = create_engine("sqlite:///shop.db")
Session = sessionmaker(bind=engine)
session = Session()

print("1. Продукты дороже 1000 рублей:")
products = session.query(Product).filter(Product.price > 1000).all()

for product in products:
    print(f" - {product.name}: {product.price} руб.")
print()


print("2. Клиенты с email в домене example.com:")
customers = session.query(Customer).filter(
    Customer.email.like("%@example.com")
).all()

for customer in customers:
    print(
        f" - {customer.first_name} {customer.last_name}: "
        f"{customer.email}"
    )
print()


print("3. Заказы со статусом pending:")
orders = session.query(Order).filter(Order.status == "pending").all()

for order in orders:
    print(
        f" - Заказ №{order.id}: "
        f"{order.total_amount} руб., статус: {order.status}"
    )
print()

print("4. Продукты категории Электроника:")
products = session.query(Product).filter(
    Product.category == "Электроника"
).all()

for product in products:
    print(f" - {product.name}: {product.price} руб.")
print()

print("5. Клиент с email maria@example.com:")
customers = session.query(Customer).filter(
    Customer.email == "maria@example.com"
).all()

for customer in customers:
    print(
        f" - {customer.first_name} {customer.last_name}: "
        f"{customer.email}"
    )
print()


print("6. Заказы на сумму больше 10000 рублей:")
orders = session.query(Order).filter(
    Order.total_amount > 10000
).all()

for order in orders:
    print(
        f" - Заказ №{order.id}: "
        f"{order.total_amount} руб., статус: {order.status}"
    )
print()


session.close()