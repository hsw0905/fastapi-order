from pydantic import BaseModel

from core.domains.product.enum.product_enum import ProductType, ProductSellingStatus


class ProductResponse(BaseModel):
    id: int
    product_number: str
    type: ProductType
    selling_status: ProductSellingStatus
    name: str
    price: int
