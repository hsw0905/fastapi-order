from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from core.persistence.models.base import Base
from core.persistence.models.base_time import BaseTimeModel


class OrderProductModel(Base, BaseTimeModel):
    __tablename__ = "order_products"

    order_id = mapped_column(ForeignKey("orders.id"), nullable=False, index=True)
    product_id = mapped_column(ForeignKey("products.id"), nullable=False, index=True)
