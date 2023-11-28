import random

import factory.alchemy
from faker import Factory as FakerFactory

from app.utils.time_helper import get_server_timestamp
from core.domains.product.enum.product_enum import ProductType, ProductSellingStatus, OrderStatus
from core.persistence.models.order_model import OrderModel
from core.persistence.models.order_product_model import OrderProductModel
from core.persistence.models.product_model import ProductModel

faker = FakerFactory.create(locale="ko_KR")


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True


class ProductFactory(BaseFactory):
    class Meta:
        model = ProductModel

    id = factory.Sequence(lambda n: n + 1)
    product_number = factory.Sequence(lambda n: f"00{n}")
    type = ProductType.HANDMADE
    selling_status = ProductSellingStatus.SELLING
    name = "아메리카노"
    price = random.randint(4000, 6000)

    @factory.post_generation
    def order_products(obj, create, extracted, **kwargs):
        if extracted:
            OrderProductFactory(products=obj, **kwargs)


class OrderFactory(BaseFactory):
    class Meta:
        model = OrderModel

    id = factory.Sequence(lambda n: n + 1)
    order_status = OrderStatus.INIT
    total_price = random.randint(6000, 10000)
    registered_date_time = get_server_timestamp()

    @factory.post_generation
    def order_products(obj, create, extracted, **kwargs):
        if extracted:
            OrderProductFactory(orders=obj, **kwargs)


class OrderProductFactory(BaseFactory):
    class Meta:
        model = OrderProductModel

    id = factory.Sequence(lambda n: n + 1)

