from sqlalchemy.orm import Session

from db.models.emitente import Emitente
from db.models.nfe import NFe as NFeModel
from db.models.product import Product as ProductModel
from db.models.transportadora import Transportadora
from schemas.nfe import NFeCreate

def save_nfe(db: Session, nfe_data: NFeCreate):
    # Cria emitente primeiro
    emitente_obj = Emitente(**nfe_data.emitente.dict())
    db.add(emitente_obj)
    db.flush()  # para gerar o id do emitente

    # Cria NFe com referência ao emitente
    nfe = NFeModel(**nfe_data.dict(exclude={"produtos", "transportadora", "emitente"}), emitente_id=emitente_obj.id)
    db.add(nfe)
    db.flush()

    # Adiciona produtos
    for prod in nfe_data.produtos:
        produto = ProductModel(**prod.dict(), nfe_id=nfe.id)
        db.add(produto)

    # Adiciona transportadora, se existir
    if nfe_data.transportadora:
        transportadora_obj = Transportadora(**nfe_data.transportadora.dict(), nfe_id=nfe.id)
        db.add(transportadora_obj)

    db.commit()
    db.refresh(nfe)
    return nfe



def get_nfe_by_chave(db: Session, chave: str):
    return db.query(NFeModel).filter(NFeModel.chave_acesso == chave).first()
