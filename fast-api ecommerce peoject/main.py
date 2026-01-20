# FastAPI application entry point

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from product_routes import router as product_router
from config import BASE_URL

app = FastAPI(
    title="Product Management API",
    version="1.0.0",
)

# API router
app.include_router(product_router)


@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to FastAPI",
            "data_path": BASE_URL,
        },
    )
