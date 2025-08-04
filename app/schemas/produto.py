from pydantic import BaseModel
from decimal import Decimal
from typing import List
from app.schemas.imposto import Imposto, ImpostoCreate


class ProdutoBase(BaseModel):
    codigo: str
    descricao: str
    quantidade: Decimal
    valor_unitario: Decimal
    valor_total: Decimal
    impostos: List[ImpostoCreate] = []

    class Config:
        from_attributes = True


class ProdutoCreate(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id: int
    impostos: List[Imposto]
