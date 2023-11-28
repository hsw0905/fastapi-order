from sqlalchemy import VARCHAR, Enum, DECIMAL
from sqlalchemy.orm import mapped_column, relationship, backref

from core.domains.product.enum.product_enum import ProductType, ProductSellingStatus
from core.persistence.models.base import Base
from core.persistence.models.base_time import BaseTimeModel


class ProductModel(Base, BaseTimeModel):
    __tablename__ = "products"

    product_number = mapped_column(VARCHAR(100))
    type = mapped_column(Enum(ProductType))
    selling_status = mapped_column(Enum(ProductSellingStatus))
    name = mapped_column(VARCHAR(100))
    price = mapped_column(DECIMAL(precision=10, scale=2))

    order_products = relationship("OrderProductModel", backref=backref("products"))
