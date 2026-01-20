# Contains all product-related functions

import json
from pathlib import Path
from typing import List, Dict

# Path to the JSON file that stores all product data
DATA_FILE = Path(__file__).parent / "products.json"


# Reads all products from the JSON file.
# use for loading products from the JSON file whenever the user makes a get request
def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Writes a list of products to the JSON file.
# use for saving products to the JSON file after adding , updating or removing a product
def save_products(products: List[Dict]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2, ensure_ascii=False)


# Returns all products as a list.
# use to show all products or to show a single product.
def get_all_products() -> List[Dict]:
    return load_products()


# Adds a new product to the JSON file.
# use on POST request, to create a new product.
def add_product(product: Dict) -> Dict:
    products = get_all_products()
    if any(p["sku"] == product["sku"] for p in products):
        raise ValueError("SKU already exists")
    products.append(product)
    save_products(products)
    return product


# Deletes a product by its ID.
# use on DELETE request, to remove a product by using its ID.
def remove_product(product_id: str):
    products = get_all_products()
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted = products.pop(index)
            save_products(products)
            return {"message": "Product deleted successfully", "data": deleted}
    raise ValueError("Product not found")


# Updates fields of an existing product.
# use on PUT request, to modify product details by using its ID
def update_product(product_id: str, payload: dict):
    products = get_all_products()
    for index, product in enumerate(products):
        if product["id"] == product_id:
            product.update(payload)
            products[index] = product
            save_products(products)
            return product
    raise ValueError("Product not found")
