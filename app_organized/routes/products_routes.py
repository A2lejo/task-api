from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app_organized.models.models import ProductCreate
from app_organized.services.products_service import list_products, register_product, change_stock

router = APIRouter(prefix="/products")

class StockUpdate(BaseModel):
    stock: int

@router.get("")
def get_products():
    return list_products()

@router.post("")
def create_product_endpoint(data: ProductCreate):
    return register_product(data)

@router.put("/{product_id}/stock")
def update_stock_endpoint(product_id: int, data: StockUpdate):
    product = change_stock(product_id, data.stock)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product