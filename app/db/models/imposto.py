from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Imposto(Base):
    __tablename__ = "impostos"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # ICMS, IPI, PIS, COFINS, etc.
    grupo = Column(String, nullable=True)  # ICMS10, IPITrib, etc
    chave = Column(String, nullable=True)  # vICMS, vIPI ...
    valor = Column(Numeric(14, 2), nullable=False)

    product_id = Column(Integer, ForeignKey("produtos.id"))
    produto = relationship("Produtos", back_populates="impostos")
