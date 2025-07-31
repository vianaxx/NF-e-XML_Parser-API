from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class ImpostoBase(BaseModel):
    tipo: str
    grupo: Optional[str]
    chave: Optional[str]
    valor: Decimal

    class Config:
        from_attributese = True

class ImpostoCreate(ImpostoBase):
    pass

class Imposto(ImpostoBase):
    id: int