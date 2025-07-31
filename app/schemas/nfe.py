from pydantic import BaseModel, constr
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from app.schemas.emitente import EmitenteCreate, Emitente
from app.schemas.destinatario import DestinatarioCreate, Destinatario
from app.schemas.transportadora import TransportadoraCreate, Transportadora
from app.schemas.product import ProductCreate, Product


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

    class Config:
        from_attributes = True


class NFeCreate(NFeBase):
    pass


class NFe(NFeBase):
    id: int
    produtos: List[Product]
    transportadora: Optional[Transportadora]
    emitente: Emitente
    destinatario: Destinatario
