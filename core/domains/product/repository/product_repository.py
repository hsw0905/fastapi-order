from sqlalchemy import select

from app.database.sqlalchemy import session
from core.domains.product.enum.product_enum import ProductSellingStatus
from core.domains.product.service.response.product_response import ProductResponse
from core.persistence.models.product_model import ProductModel


class ProductRepository:
    def find_all_by_selling_type_in(
        self, selling_status_list: list[ProductSellingStatus]
    ) -> list[ProductResponse]:
        statement = select(ProductModel).where(
            ProductModel.selling_status.in_(selling_status_list)
        )

        products = session.execute(statement).scalars().all()

        return [product for product in products]
