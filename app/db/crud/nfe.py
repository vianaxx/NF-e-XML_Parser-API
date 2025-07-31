from sqlalchemy.orm import Session
from app.db.models.nfe import NFe
from app.db.models.emitente import Emitente
from app.db.models.destinatario import Destinatario
from app.db.models.transportadora import Transportadora
from app.db.models.product import Product
from app.db.models.imposto import Imposto
from app.schemas.nfe import NFeCreate
from decimal import Decimal


def get_or_create_emitente(db: Session, emitente_data):
    instance = db.query(Emitente).filter_by(cnpj=emitente_data.cnpj).first()
    if instance:
        return instance
    instance = Emitente(**emitente_data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def get_or_create_destinatario(db: Session, destinatario_data):
    instance = db.query(Destinatario).filter_by(cnpj=destinatario_data.cnpj).first()
    if instance:
        return instance
    instance = Destinatario(**destinatario_data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def get_or_create_transportadora(db: Session, transportadora_data):
    if transportadora_data is None:
        return None
    instance = db.query(Transportadora).filter_by(cnpj=transportadora_data.cnpj).first()
    if instance:
        return instance
    instance = Transportadora(**transportadora_data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def get_or_create_product(db: Session, product_data):
    instance = db.query(Product).filter_by(codigo=product_data.codigo).first()
    if instance:
        return instance
    instance = Product(
        codigo=product_data.codigo,
        descricao=product_data.descricao,
        quantidade=product_data.quantidade,
        valor_unitario=product_data.valor_unitario,
        valor_total=product_data.valor_total
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def save_nfe(db: Session, nfe_data: NFeCreate):
    emitente = get_or_create_emitente(db, nfe_data.emitente)
    destinatario = get_or_create_destinatario(db, nfe_data.destinatario)
    transportadora = get_or_create_transportadora(db, nfe_data.transportadora)

    nfe = NFe(
        chave_acesso=nfe_data.chave_acesso,
        numero=nfe_data.numero,
        serie=nfe_data.serie,
        data_emissao=nfe_data.data_emissao,
        valor_total=nfe_data.valor_total,
        emitente_cnpj=emitente.cnpj,
        destinatario_cnpj=destinatario.cnpj,
        transportadora=transportadora
    )
    db.add(nfe)
    db.commit()
    db.refresh(nfe)

    # products + impostos
    for prod_data in nfe_data.produtos:
        produto = Product(
            codigo=prod_data.codigo,
            descricao=prod_data.descricao,
            quantidade=prod_data.quantidade,
            valor_unitario=prod_data.valor_unitario,
            valor_total=prod_data.valor_total,
            nfe_id=nfe.id
        )
        db.add(produto)
        db.commit()
        db.refresh(produto)
        for imp_data in prod_data.impostos:
            imposto = Imposto(
                tipo=imp_data.tipo,
                grupo=getattr(imp_data, "grupo", None),
                chave=getattr(imp_data, "chave", None),
                valor=imp_data.valor,
                product_id=produto.id
            )
            db.add(imposto)
        db.commit()

    db.refresh(nfe)
    return nfe
