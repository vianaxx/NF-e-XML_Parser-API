from sqlalchemy.orm import Session

from db.models.destinatario import Destinatario
from db.models.emitente import Emitente
from db.models.nfe import NFe as NFeModel
from db.models.product import Product as ProductModel
from db.models.transportadora import Transportadora
from db.models.imposto import Imposto  # <- Novo
from schemas.nfe import NFeCreate


def save_nfe(db: Session, nfe_data: NFeCreate):
    # 🏭 Emitente
    emitente_obj = Emitente(**nfe_data.emitente.dict())
    db.add(emitente_obj)
    db.flush()

    # 🧾 Destinatário (evita duplicidade via CNPJ)
    destinatario_data = nfe_data.destinatario

    dest_obj = db.query(Destinatario).filter_by(cnpj=destinatario_data.cnpj).first()
    if not dest_obj:
        dest_obj = Destinatario(**destinatario_data.dict())
        db.add(dest_obj)
        db.flush()

    # 📄 NF-e principal
    nfe = NFeModel(
        **nfe_data.dict(exclude={"produtos", "transportadora", "emitente", "destinatario"}),
        emitente_id=emitente_obj.id,
        destinatario_cnpj=dest_obj.cnpj
    )
    db.add(nfe)
    db.flush()

    # 📦 Produtos + 🧾 Impostos
    for prod in nfe_data.produtos:
        produto = ProductModel(**prod.dict(exclude={"impostos"}), nfe_id=nfe.id)
        db.add(produto)
        db.flush()

        for imposto_data in prod.impostos:
            imposto = Imposto(
                tipo=imposto_data.tipo,
                valor=imposto_data.valor,
                product_id=produto.id
            )
            db.add(imposto)

    # 🚚 Transportadora (opcional)
    if nfe_data.transportadora:
        transportadora_obj = Transportadora(
            **nfe_data.transportadora.dict(),
            nfe_id=nfe.id
        )
        db.add(transportadora_obj)

    db.commit()
    db.refresh(nfe)
    return nfe


def get_nfe_by_chave(db: Session, chave: str):
    return db.query(NFeModel).filter(NFeModel.chave_acesso == chave).first()
