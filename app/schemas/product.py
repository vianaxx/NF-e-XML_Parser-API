from pydantic import BaseModel
from decimal import Decimal
from typing import List
from app.schemas.imposto import Imposto, ImpostoCreate


class ProductBase(BaseModel):
    codigo: str
    descricao: str
    quantidade: Decimal
    valor_unitario: Decimal
    valor_total: Decimal
    impostos: List[ImpostoCreate] = []

    class Config:
        from_attributes = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    impostos: List[Imposto]
