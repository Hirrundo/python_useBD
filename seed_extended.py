from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models_extended import Product, Customer, Order

engine = create_engine("sqlite:///shop_extended.db")
Session = sessionmaker(bind=engine)
session = Session()


laptop = Product(
    name="Ноутбук",
    price=50000,
    category="Электроника"
)

smartphone = Product(
    name="Смартфон",
    price=30000,
    category="Электроника"
)

book = Product(
    name="Книга",
    price=500,
    category="Литература"
)

tshirt = Product(
    name="Футболка",
    price=1500,
    category="Одежда"
)

coffee = Product(
    name="Кофе",
    price=400,
    category="Продукты"
)


ivan = Customer(
    first_name="Иван",
    last_name="Петров",
    email="ivan@example.com"
)

maria = Customer(
    first_name="Мария",
    last_name="Иванова",
    email="maria@example.com"
)

alex = Customer(
    first_name="Алексей",
    last_name="Сидоров",
    email="alex@example.com"
)


order1 = Order(
    customer=ivan,
    total_amount=50500,
    status="completed",
    products=[laptop, book]
)

order2 = Order(
    customer=maria,
    total_amount=1500,
    status="pending",
    products=[tshirt]
)

order3 = Order(
    customer=alex,
    total_amount=400,
    status="shipped",
    products=[coffee]
)

order4 = Order(
    customer=ivan,
    total_amount=30000,
    status="pending",
    products=[smartphone]
)


session.add_all([
    laptop,
    smartphone,
    book,
    tshirt,
    coffee,
    ivan,
    maria,
    alex,
    order1,
    order2,
    order3,
    order4
])


session.commit()

print(f"Продуктов: {session.query(Product).count()}")
print(f"Клиентов: {session.query(Customer).count()}")
print(f"Заказов: {session.query(Order).count()}")

session.close()