from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, constr

from schemas.destinatario import DestinatarioCreate, Destinatario
from schemas.emitente import EmitenteCreate, Emitente
from schemas.product import Product, ProductCreate
from schemas.transportadora import Transportadora, TransportadoraCreate


class NFeBase(BaseModel):
    chave_acesso: constr(min_length=44, max_length=44)
    numero: str
    serie: str
    data_emissao: datetime
    valor_total: Decimal
    produtos: List[ProductCreate]
    transportadora: Optional[TransportadoraCreate]
    emitente: EmitenteCreate
    destinatario: DestinatarioCreate


class NFeCreate(NFeBase):
    pass


class NFe(NFeBase):
    id: int
    produtos: List[Product]
    transportadora: Optional[Transportadora]
    emitente: Emitente
    destinatario: Destinatario

    class Config:
        from_attributes = True
