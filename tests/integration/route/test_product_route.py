from sqlalchemy.orm import scoped_session, Session
from starlette.testclient import TestClient

from tests.seeder.factory import ProductFactory


def test_should_get_selling_products(test_session: scoped_session[Session], client: TestClient):
    product_1 = ProductFactory.create()
    product_2 = ProductFactory.create()
    product_3 = ProductFactory.create()

    response = client.get("/api/v1/products/selling")

    for elm in response.json():
        assert "id" in elm
        assert "product_number" in elm
        assert "type" in elm
        assert "name" in elm
        assert "price" in elm
