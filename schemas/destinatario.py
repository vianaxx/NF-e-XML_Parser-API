from pydantic import BaseModel, constr
from typing import Optional


class DestinatarioBase(BaseModel):
    cnpj: constr(min_length=14, max_length=14)
    nome: str
    ie: Optional[str] = None
    endereco: Optional[str] = None


class DestinatarioCreate(DestinatarioBase):
    pass


class Destinatario(DestinatarioBase):
    class Config:
        from_attributes = True
