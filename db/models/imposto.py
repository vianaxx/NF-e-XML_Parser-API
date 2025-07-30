from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Imposto(Base):
    __tablename__ = "impostos"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # Ex: ICMS, IPI, PIS, COFINS
    valor = Column(Numeric(10, 2), nullable=False)

    product_id = Column(Integer, ForeignKey("product.id"))
    produto = relationship("Product", back_populates="impostos")
