from decimal import Decimal
from pydantic import BaseModel

class ProductBase(BaseModel):
    codigo: str
    descricao: str
    quantidade: Decimal
    valor_unitario: Decimal
    valor_total: Decimal

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
