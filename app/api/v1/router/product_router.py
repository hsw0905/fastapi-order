from fastapi import APIRouter

from core.domains.product.service.product_service import ProductService

product_router = APIRouter()


@product_router.get("/selling")
def get_selling_products():
    return ProductService().get_selling_products()
