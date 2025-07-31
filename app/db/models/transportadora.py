from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Transportadora(Base):
    __tablename__ = "transportadora"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), nullable=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String, nullable=True)
    ie = Column(String, nullable=True)
    endereco = Column(String, nullable=True)

    nfe_id = Column(Integer, ForeignKey("nfe.id"))
    nfe = relationship(
        "NFe",
        back_populates="transportadora",
        foreign_keys=[nfe_id]
    )

