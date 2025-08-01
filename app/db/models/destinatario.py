from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base


class Destinatario(Base):
    __tablename__ = "destinatarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cnpj = Column(String, index=True, nullable=True)
    nome = Column(String, nullable=False)
    ie = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    numero = Column(String, nullable=True)
    bairro = Column(String, nullable=True)
    municipio = Column(String, nullable=True)
    codigo_municipio = Column(String, nullable=True)
    uf = Column(String, nullable=True)
    cep = Column(String, nullable=True)
    codigo_pais = Column(String, nullable=True)
    pais = Column(String, nullable=True)

    nfes = relationship("NFe", back_populates="destinatario", uselist=False)

    __table_args__ = (
        UniqueConstraint(
            "cnpj", "endereco", "numero", "bairro", "municipio", "uf", "cep",
            name="uix_destinatario_unico"
        ),
    )
