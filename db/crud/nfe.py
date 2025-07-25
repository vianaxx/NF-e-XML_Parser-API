from sqlalchemy.orm import Session
from db.models.nfe import NFe as NFeModel
from db.models.product import Product as ProductModel
from schemas.nfe import NFeCreate

def save_nfe(db: Session, nfe_data: NFeCreate):
    nfe = NFeModel(**nfe_data.dict(exclude={"produtos"}))
    db.add(nfe)
    db.flush()  # Garante ID para o relacionamento

    for prod in nfe_data.produtos:
        produto = ProductModel(**prod.dict(), nfe_id=nfe.id)
        db.add(produto)

    db.commit()
    db.refresh(nfe)
    return nfe

def get_nfe_by_chave(db: Session, chave: str):
    return db.query(NFeModel).filter(NFeModel.chave_acesso == chave).first()
