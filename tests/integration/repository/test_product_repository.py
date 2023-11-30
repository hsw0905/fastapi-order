from sqlalchemy.orm import scoped_session, Session

from core.domains.product.enum.product_enum import ProductSellingStatus
from core.domains.product.repository.product_repository import ProductRepository
from tests.seeder.factory import ProductFactory


def test_should_get_selling_status_product(test_session: scoped_session[Session]) -> None:
    product_1 = ProductFactory.create()
    product_2 = ProductFactory.create()
    product_3 = ProductFactory.create()

    repository = ProductRepository()
    result = repository.find_all_by_selling_type_in([ProductSellingStatus.SELLING, ProductSellingStatus.HOLD])

    assert len(result) == 3
    
