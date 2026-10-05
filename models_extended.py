from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table,
    func
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


order_product = Table(
    "order_product",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True)
)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String(50))

    # Связь с заказами
    orders = relationship(
        "Order",
        secondary=order_product,
        back_populates="products"
    )


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

  
    orders = relationship(
        "Order",
        back_populates="customer"
    )


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, server_default=func.now())
    total_amount = Column(Integer, nullable=False)
    status = Column(String(20), default="pending")

    
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship(
        "Customer",
        back_populates="orders"
    )

    
    products = relationship(
        "Product",
        secondary=order_product,
        back_populates="orders"
    )


engine = create_engine("sqlite:///shop_extended.db")


Base.metadata.create_all(engine)