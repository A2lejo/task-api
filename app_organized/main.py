from fastapi import FastAPI
from app_organized.routes.products_routes import router
from app_organized.routes.customer_routes import router as customer_router
from app_organized.config import get_setting

app = FastAPI(
    title=get_setting("APP_NAME", "API Modular"),
    description="Una API organizada por capas aplicando principios de diseño para gestionar productos y clientes en un sistema de inventario",
    version=get_setting("APP_VERSION", "1.0.0")
)
app.include_router(router)
app.include_router(customer_router)

@app.get("/")
def home():
    return {"message": "API modular de inventario lista", "docs": "/docs", "base_path": "/products"} 

@app.get("/system/info")
def system_info():
    return {
        "application": get_setting("APP_NAME", "API Modular"),
        "version": get_setting("APP_VERSION", "1.0.0"),
        "environment": get_setting("ENVIRONMENT", "DEV"),
        "author": get_setting("AUTHOR", "No definido")
    }