from pydantic import BaseModel, constr
from typing import Optional

class EmitenteBase(BaseModel):
    cnpj: constr(min_length=14, max_length=14)
    nome: Optional[str]
    fantasia: Optional[str]
    ie: Optional[str]
    crt: Optional[str]
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

class EmitenteCreate(EmitenteBase):
    pass

class Emitente(EmitenteBase):
    pass

