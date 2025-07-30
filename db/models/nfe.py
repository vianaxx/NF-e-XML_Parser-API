from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class NFe(Base):
    __tablename__ = "nfe"

    id = Column(Integer, primary_key=True, index=True)
    chave_acesso = Column(String(44), unique=True, index=True, nullable=False)
    numero = Column(String, nullable=False)
    serie = Column(String, nullable=False)
    data_emissao = Column(DateTime, nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)

    emitente_id = Column(Integer, ForeignKey("emitente.id"), nullable=False)
    emitente = relationship("Emitente", back_populates="nfe", uselist=False)

    destinatario_cnpj = Column(String(14), ForeignKey("destinatarios.cnpj"))
    destinatario = relationship("Destinatario", back_populates="nfe", lazy="joined")

    produtos = relationship("Product", back_populates="nfe", cascade="all, delete-orphan")
    transportadora = relationship("Transportadora", back_populates="nfe", uselist=False, cascade="all, delete-orphan")
