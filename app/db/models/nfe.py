from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class NFe(Base):
    __tablename__ = "nfe"

    id = Column(Integer, primary_key=True, index=True)
    chave_acesso = Column(String(44), unique=True, index=True, nullable=False)
    numero = Column(String, nullable=False)
    serie = Column(String, nullable=False)
    data_emissao = Column(DateTime, nullable=False)
    valor_total = Column(Numeric(14, 2), nullable=False)

    emitente_id = Column(Integer, ForeignKey("emitentes.id"))
    destinatario_id = Column(Integer, ForeignKey("destinatarios.id"))
    entrega_id = Column(Integer, ForeignKey("entregas.id"))
    transportadora_id = Column(Integer, ForeignKey("transportadoras.id"))

    emitente = relationship("Emitente", back_populates="nfes")
    destinatario = relationship("Destinatario", back_populates="nfes")
    entrega = relationship("Entrega", back_populates="nfes")
    transportadora = relationship("Transportadora", back_populates="nfes")

    produtos = relationship("Produtos", back_populates="nfe", cascade="all, delete-orphan")
