from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    quantidade = Column(Numeric(14, 2), nullable=False)
    valor_unitario = Column(Numeric(14, 2), nullable=False)
    valor_total = Column(Numeric(14, 2), nullable=False)

    nfe_id = Column(Integer, ForeignKey("nfe.id"))
    nfe = relationship("NFe", back_populates="produtos")

    impostos = relationship("Imposto", back_populates="produto", cascade="all, delete-orphan")