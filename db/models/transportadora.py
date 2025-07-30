from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Transportadora(Base):
    __tablename__ = "transportadora"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), nullable=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String, nullable=True)
    ie = Column(String, nullable=True)  # inscrição estadual
    endereco = Column(String, nullable=True)

    nfe_id = Column(Integer, ForeignKey("nfe.id"))
    nfe = relationship("NFe", back_populates="transportadora")
