from sqlalchemy import Column, String, Integer
from app.db.base import Base
from sqlalchemy.orm import relationship


class Emitente(Base):
    __tablename__ = "emitentes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cnpj = Column(String(20), unique=True, nullable=False)
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

    nfes = relationship("NFe", back_populates="emitente")
