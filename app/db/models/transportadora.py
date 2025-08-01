from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Transportadora(Base):
    __tablename__ = "transportadoras"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, unique=True, index=True, nullable=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String, nullable=True)
    ie = Column(String, nullable=True)
    endereco = Column(String, nullable=True)

    nfes = relationship("NFe", back_populates="transportadora")

