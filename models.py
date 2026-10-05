from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///shop.db")


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String(50))

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, server_default=func.now())
    total_amount = Column(Integer, nullable=False)
    status = Column(String(20), default="pending")

Base.metadata.create_all(engine)