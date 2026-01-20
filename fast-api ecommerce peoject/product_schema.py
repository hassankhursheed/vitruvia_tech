# Contains all Product-related Pydantic schemas

from pydantic import (
    BaseModel,
    Field,
    AnyUrl,
    field_validator,
    model_validator,
    computed_field,
    EmailStr,
)
from typing import Annotated, Literal, Optional, List
from uuid import UUID
from datetime import datetime



# nested schemas to be used in the main schema, based on validation rules of each field

class DimensionsCM(BaseModel):
    length: Annotated[float, Field(gt=0, description="Length in cm")]
    width: Annotated[float, Field(gt=0, description="Width in cm")]
    height: Annotated[float, Field(gt=0, description="Height in cm")]


class Seller(BaseModel):
    id: UUID
    name: Annotated[str, Field(min_length=2, max_length=60)]
    email: EmailStr
    website: AnyUrl

    @field_validator("email", mode="after")
    @classmethod
    def validate_email_domain(cls, value: EmailStr):
        allowed_domains = {
            "mistore.in", "realmeofficial.in", "samsungindia.in",
            "lenovostore.in", "hpworld.in", "applestoreindia.in",
            "dellexclusive.in", "sonycenter.in",
            "oneplusstore.in", "asusexclusive.in",
        }
        domain = value.split("@")[-1].lower()
        if domain not in allowed_domains:
            raise ValueError(f"Seller email domain not allowed: {domain}")
        return value


# main schema to be used in the API endpoints
class Product(BaseModel):
    id: UUID
    sku: str
    name: str
    description: str
    category: str
    brand: str
    price: float
    currency: Literal["INR"] = "INR"
    discount_percent: int = 0
    stock: int
    is_active: bool
    rating: float
    tags: Optional[List[str]]
    image_urls: List[AnyUrl]
    dimensions_cm: DimensionsCM
    seller: Seller
    created_at: datetime

    @model_validator(mode="after")
    @classmethod
    def validate_rules(cls, model):
        if model.stock == 0 and model.is_active:
            raise ValueError("Product with zero stock cannot be active")
        return model

    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * (1 - self.discount_percent / 100), 2)


# update schemas to update existing products

class DimensionsCMUpdate(BaseModel):
    length: Optional[float]
    width: Optional[float]
    height: Optional[float]


class SellerUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    website: Optional[AnyUrl]


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    brand: Optional[str]
    price: Optional[float]
    discount_percent: Optional[int]
    stock: Optional[int]
    is_active: Optional[bool]
    rating: Optional[float]
    tags: Optional[List[str]]
    image_urls: Optional[List[AnyUrl]]
    dimensions_cm: Optional[DimensionsCMUpdate]
    seller: Optional[SellerUpdate]
