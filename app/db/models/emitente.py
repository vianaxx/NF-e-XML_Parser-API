
from sqlalchemy import Column, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class Emitente(Base):
    __tablename__ = "emitente"

    cnpj = Column(String(14), primary_key=True, index=True)
    nome = Column(String, nullable=True)
    fantasia = Column(String, nullable=True)
    ie = Column(String, nullable=True)
    crt = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    numero = Column(String, nullable=True)
    bairro = Column(String, nullable=True)
    municipio = Column(String, nullable=True)
    codigo_municipio = Column(String, nullable=True)
    uf = Column(String, nullable=True)
    cep = Column(String, nullable=True)
    codigo_pais = Column(String, nullable=True)
    pais = Column(String, nullable=True)

    nfe = relationship("NFe", back_populates="emitente")