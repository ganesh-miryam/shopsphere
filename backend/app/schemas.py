from typing import Optional
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    class ConfigDict:
        from_attributes = True