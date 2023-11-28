from sqlalchemy import Enum, DECIMAL, DateTime
from sqlalchemy.orm import mapped_column, relationship, backref

from core.domains.product.enum.product_enum import OrderStatus
from core.persistence.models.base import Base
from core.persistence.models.base_time import BaseTimeModel


class OrderModel(Base, BaseTimeModel):
    __tablename__ = "orders"

    order_status = mapped_column(Enum(OrderStatus))
    total_price = mapped_column(DECIMAL(precision=10, scale=2))
    registered_date_time = mapped_column(DateTime)

    order_products = relationship("OrderProductModel", backref=backref("orders"))
