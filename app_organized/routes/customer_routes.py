from fastapi import APIRouter
from app_organized.models.models import CustomerCreate
from app_organized.services.customer_service import (
    list_customers,
    register_customer, 
    disable_customer
)
from app_organized.utils.validators import validate_exists
from app_organized.utils.logger import logger


router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("")
def get_customers():
    logger.info("Listing all customers")
    return list_customers()

@router.post("")
def create_customer_endpoint(data: CustomerCreate):
    customer = register_customer(data)
    logger.info(f"Cliente registrado: {customer.email}")
    return customer
    
@router.put("/{customer_id}/deactivate")
def deactivate(customer_id: int):
    customer = disable_customer(customer_id)
    customer = validate_exists(customer, "Cliente no encontrado")
    logger.info(f"Cliente desactivado: {customer.email}")
    return customer 