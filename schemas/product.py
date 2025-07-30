from decimal import Decimal
from typing import List

from pydantic import BaseModel

from schemas.imposto import ImpostoCreate, Imposto


class ProductBase(BaseModel):
    codigo: str
    descricao: str
    quantidade: Decimal
    valor_unitario: Decimal
    valor_total: Decimal
    impostos: List[ImpostoCreate] = []

class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    impostos: List[Imposto]

    class Config:
        from_attributes = True
