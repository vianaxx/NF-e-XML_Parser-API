from sqlalchemy.orm import Session

from db.models.destinatario import Destinatario
from db.models.emitente import Emitente
from db.models.nfe import NFe as NFeModel
from db.models.product import Product as ProductModel
from db.models.transportadora import Transportadora
from schemas.nfe import NFeCreate


def save_nfe(db: Session, nfe_data: NFeCreate):
    # Emitente
    emitente_obj = Emitente(**nfe_data.emitente.dict())
    db.add(emitente_obj)
    db.flush()

    # Destinatário
    destinatario_data = nfe_data.destinatario
    dest_obj = db.query(Destinatario).filter_by(cnpj=destinatario_data.cnpj).first()
    if not dest_obj:
        dest_obj = Destinatario(**destinatario_data.dict())
        db.add(dest_obj)
        db.flush()

    # NFe
    nfe = NFeModel(
        **nfe_data.dict(exclude={"produtos", "transportadora", "emitente", "destinatario"}),
        emitente_id=emitente_obj.id,
        destinatario_cnpj=dest_obj.cnpj
    )
    db.add(nfe)
    db.flush()

    # Produtos
    for prod in nfe_data.produtos:
        produto = ProductModel(**prod.dict(), nfe_id=nfe.id)
        db.add(produto)

    # Transportadora
    if nfe_data.transportadora:
        transportadora_obj = Transportadora(**nfe_data.transportadora.dict(), nfe_id=nfe.id)
        db.add(transportadora_obj)

    db.commit()
    db.refresh(nfe)
    return nfe


def get_nfe_by_chave(db: Session, chave: str):
    return db.query(NFeModel).filter(NFeModel.chave_acesso == chave).first()
