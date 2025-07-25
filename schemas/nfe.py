from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, constr
from schemas.product import Product, ProductCreate

class NFeBase(BaseModel):
    chave_acesso: constr(min_length=44, max_length=44)
    numero: str
    serie: str
    data_emissao: datetime
    cnpj_emitente: constr(min_length=14, max_length=14)
    nome_emitente: str
    cnpj_destinatario: Optional[constr(min_length=11, max_length=14)]
    nome_destinatario: Optional[str]
    valor_total: Decimal
    produtos: List[ProductCreate]

class NFeCreate(NFeBase):
    pass

class NFe(NFeBase):
    id: int
    produtos: List[Product]

    class Config:
        orm_mode = True
