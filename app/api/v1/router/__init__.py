from fastapi import APIRouter

from app.api.v1.router.product_router import product_router

v1_router = APIRouter()

v1_router.include_router(product_router, prefix="/api/v1/products", tags=["Product"])
