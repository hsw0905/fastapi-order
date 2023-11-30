from sqlalchemy.orm import scoped_session, Session

from core.domains.product.service.product_service import ProductService
from tests.seeder.factory import ProductFactory


def test_should_get_selling_products(test_session: scoped_session[Session]):
    product_1 = ProductFactory.create()
    product_2 = ProductFactory.create()
    product_3 = ProductFactory.create()

    service = ProductService()

    responses = service.get_selling_products()

    assert len(responses) == 3
