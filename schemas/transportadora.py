from typing import Optional
from pydantic import BaseModel, constr

class TransportadoraBase(BaseModel):
    cnpj: Optional[constr(min_length=14, max_length=14)]
    cpf: Optional[constr(min_length=11, max_length=11)]
    nome: Optional[str]
    ie: Optional[str]
    endereco: Optional[str]

class TransportadoraCreate(TransportadoraBase):
    pass

class Transportadora(TransportadoraBase):
    id: int

    class Config:
        from_attributes = True
