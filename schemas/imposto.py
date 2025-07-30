from decimal import Decimal
from pydantic import BaseModel

class ImpostoBase(BaseModel):
    tipo: str
    valor: Decimal

class ImpostoCreate(ImpostoBase):
    pass

class Imposto(ImpostoBase):
    id: int

    class Config:
        from_attributes = True
