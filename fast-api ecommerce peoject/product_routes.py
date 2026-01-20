# contains all product routes for the API endpoints to be used in main.py

from fastapi import APIRouter, HTTPException, Query, Path
from uuid import UUID, uuid4
from datetime import datetime

from product_schema import Product, ProductUpdate
from product_service import (
    get_all_products,
    add_product,
    remove_product,
    update_product,
)

# API router that contains all product routes
router = APIRouter()

# API endpoints

# GET products route that returns a list of products.
# it will show all products by default but you can filter by name
@router.get("/")
def list_products(
    name: str | None = Query(None),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
):
    products = get_all_products()

    # filter by name
    if name:
        filtered_products = []
        for p in products:
            # if entered name is in product name
            if name.lower() in p["name"].lower():
                filtered_products.append(p)
        products = filtered_products

    # return the total number of products and the list of products
    return {
        "total": len(products),
        "items": products[offset : offset + limit],
    }

# GET product route that returns a single product, by searching using ID
@router.get("/{product_id}")
def get_product(product_id: UUID = Path(...)):
    for product in get_all_products():
        if product["id"] == str(product_id):
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# POST product route that creates a new product
@router.post("/", status_code=201)
def create_product(product: Product):
    data = product.model_dump(mode="json")
    data["id"] = str(uuid4())
    data["created_at"] = datetime.utcnow().isoformat() + "Z"
    return add_product(data)


# DELETE product route that deletes a product
@router.delete("/{product_id}")
def delete_product(product_id: UUID):
    return remove_product(str(product_id))


# PUT product route that updates a product
@router.put("/{product_id}")
def edit_product(product_id: UUID, payload: ProductUpdate):
    return update_product(
        str(product_id),
        payload.model_dump(exclude_unset=True),
    )
