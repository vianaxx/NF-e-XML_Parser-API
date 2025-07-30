from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class Emitente(Base):
    __tablename__ = "emitente"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14), unique=True, index=True, nullable=False)
    nome = Column(String, nullable=False)
    ie = Column(String, nullable=True)  # inscrição estadual opcional
    endereco = Column(String, nullable=True)  # opcional, se desejar armazenar

    nfe = relationship("NFe", back_populates="emitente", uselist=False)
