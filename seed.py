from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Product, Customer, Order


engine = create_engine("sqlite:///shop.db")
Session = sessionmaker(bind=engine)
session = Session()


products = [
    Product(name="Ноутбук", price=50000, category="Электроника"),
    Product(name="Смартфон", price=30000, category="Электроника"),
    Product(name="Книга", price=500, category="Литература"),
    Product(name="Футболка", price=1500, category="Одежда"),
    Product(name="Кофе", price=400, category="Продукты"),
]


customers = [
    Customer(
        first_name="Иван",
        last_name="Петров",
        email="ivan@example.com"
    ),
    Customer(
        first_name="Мария",
        last_name="Иванова",
        email="maria@example.com"
    ),
    Customer(
        first_name="Алексей",
        last_name="Сидоров",
        email="alex@example.com"
    ),
]


orders = [
    Order(total_amount=50500, status="completed"),
    Order(total_amount=1500, status="pending"),
    Order(total_amount=400, status="shipped"),
]


session.add_all(products)
session.add_all(customers)
session.add_all(orders)


session.commit()

print(f"Продуктов: {session.query(Product).count()}")
print(f"Клиентов: {session.query(Customer).count()}")
print(f"Заказов: {session.query(Order).count()}")


session.close()