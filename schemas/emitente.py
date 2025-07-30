from typing import Optional
from pydantic import BaseModel, constr


class EmitenteBase(BaseModel):
    cnpj: constr(min_length=14, max_length=14)
    nome: Optional[str]
    ie: Optional[str]
    endereco: Optional[str]


class EmitenteCreate(EmitenteBase):
    pass


class Emitente(EmitenteBase):
    id: int

    class Config:
        from_attributes = True
