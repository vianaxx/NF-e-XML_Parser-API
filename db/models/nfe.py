from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from db.database import Base

class NFe(Base):
    __tablename__ = "nfe"

    id = Column(Integer, primary_key=True, index=True)
    chave_acesso = Column(String(44), unique=True, index=True, nullable=False)
    numero = Column(String, nullable=False)
    serie = Column(String, nullable=False)
    data_emissao = Column(DateTime, nullable=False)
    cnpj_emitente = Column(String(14), nullable=False)
    nome_emitente = Column(String, nullable=False)
    cnpj_destinatario = Column(String(14), nullable=True)
    nome_destinatario = Column(String, nullable=True)
    valor_total = Column(Numeric(10, 2), nullable=False)

    produtos = relationship("Product", back_populates="nfe", cascade="all, delete-orphan")
