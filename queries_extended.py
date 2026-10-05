from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models_extended import Product, Customer, Order


engine = create_engine("sqlite:///shop_extended.db")
Session = sessionmaker(bind=engine)
session = Session()

print("1. Заказы клиента Иван Петров:")

customer = session.query(Customer).filter(
    Customer.first_name == "Иван",
    Customer.last_name == "Петров"
).first()

if customer:
    for order in customer.orders:
        print(
            f"   Заказ #{order.id}: "
            f"{order.order_date}, "
            f"статус: {order.status}, "
            f"сумма: {order.total_amount} руб."
        )

print()


print("2. Товары в заказах со статусом pending:")

orders = session.query(Order).filter(
    Order.status == "pending"
).all()

for order in orders:
    for product in order.products:
        print(
            f"   {product.name}: "
            f"{product.price} руб., "
            f"категория: {product.category}"
        )

print()


print("3. Клиенты, заказавшие товары из категории Электроника:")

customers = (
    session.query(Customer)
    .join(Customer.orders)
    .join(Order.products)
    .filter(Product.category == "Электроника")
    .distinct()
    .all()
)

for customer in customers:
    print(
        f"   {customer.first_name} "
        f"{customer.last_name}: "
        f"{customer.email}"
    )

print()

print("4. Заказы, в которых есть товар Смартфон:")

orders = (
    session.query(Order)
    .join(Order.products)
    .filter(Product.name == "Смартфон")
    .all()
)

for order in orders:
    print(
        f"   Заказ #{order.id}: "
        f"{order.order_date}, "
        f"статус: {order.status}, "
        f"клиент: {order.customer.first_name} "
        f"{order.customer.last_name}"
    )

print()


print("5. Общая сумма заказов для каждого клиента:")

totals = (
    session.query(
        Customer.first_name,
        Customer.last_name,
        func.sum(Order.total_amount).label("total_sum")
    )
    .join(Customer.orders)
    .group_by(Customer.id)
    .all()
)

for first_name, last_name, total_sum in totals:
    print(
        f"   {first_name} {last_name}: "
        f"{total_sum} руб."
    )

print()


session.close()