from fastapi import FastAPI
from app_organized.routes.products_routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de inventario lista", "docs": "/docs", "base_path": "/products"}