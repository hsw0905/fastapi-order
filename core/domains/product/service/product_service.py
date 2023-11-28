import inject

from core.domains.product.enum.product_enum import ProductSellingStatus
from core.domains.product.repository.product_repository import ProductRepository
from core.domains.product.service.response.product_response import ProductResponse


class ProductService:
    @inject.autoparams()
    def __init__(self, product_repo: ProductRepository):
        self._product_repo = product_repo

    def get_selling_products(self) -> list[ProductResponse]:
        products = self._product_repo.find_all_by_selling_type_in(
            ProductSellingStatus.for_display()
        )

        result = []
        for product in products:
            response = ProductResponse(
                id=product.id,
                product_number=product.product_number,
                type=product.type,
                name=product.name,
                price=product.price,
            )
            result.append(response)

        return result
