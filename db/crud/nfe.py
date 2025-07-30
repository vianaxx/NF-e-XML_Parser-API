from sqlalchemy.orm import Session
from db.models.nfe import NFe as NFeModel
from db.models.product import Product as ProductModel
from db.models.transportadora import Transportadora
from schemas.nfe import NFeCreate

def save_nfe(db: Session, nfe_data: NFeCreate):
    nfe = NFeModel(**nfe_data.dict(exclude={"produtos", "transportadora"}))
    db.add(nfe)
    db.flush()  # Garante ID para relacionamentos

    # Produtos
    for prod in nfe_data.produtos:
        produto = ProductModel(**prod.dict(), nfe_id=nfe.id)
        db.add(produto)

    # Transportadora (se existir)
    if nfe_data.transportadora:
        transportadora_data = nfe_data.transportadora.dict()
        transportadora = Transportadora(**transportadora_data, nfe_id=nfe.id)
        db.add(transportadora)

    db.commit()
    db.refresh(nfe)
    return nfe


def get_nfe_by_chave(db: Session, chave: str):
    return db.query(NFeModel).filter(NFeModel.chave_acesso == chave).first()
