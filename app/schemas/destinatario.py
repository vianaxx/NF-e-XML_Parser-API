from pydantic import BaseModel, constr
from typing import Optional


class DestinatarioBase(BaseModel):
    cnpj: Optional[str] = None
    nome: str
    ie: Optional[str]
    endereco: Optional[str]
    numero: Optional[str]
    bairro: Optional[str]
    municipio: Optional[str]
    codigo_municipio: Optional[str]
    uf: Optional[str]
    cep: Optional[str]
    codigo_pais: Optional[str]
    pais: Optional[str]

    class Config:
        from_attributes = True


class DestinatarioCreate(DestinatarioBase):
    pass


class Destinatario(DestinatarioBase):
    pass
