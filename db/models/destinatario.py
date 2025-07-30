from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from db.database import Base


class Destinatario(Base):
    __tablename__ = "destinatarios"

    cnpj = Column(String(14), primary_key=True, index=True)
    nome = Column(String, nullable=False)
    ie = Column(String, nullable=True)
    endereco = Column(String, nullable=True)

    nfe = relationship("NFe", back_populates="destinatario", uselist=False)
