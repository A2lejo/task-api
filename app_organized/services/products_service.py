from app_organized.data.products_repository import get_all_products, create_product, update_stock

def list_products():
    return get_all_products()

def register_product(data):
    return create_product(data)

def change_stock(product_id: int, stock: int):
    return update_stock(product_id, stock)