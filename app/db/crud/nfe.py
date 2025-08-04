from sqlalchemy.orm import Session

from app.db.crud.destinatario import get_or_create_destinatario
from app.db.crud.emitente import get_or_create_emitente
from app.db.crud.transportadora import get_or_create_transportadora
from app.db.models.nfe import NFe
from app.db.models.emitente import Emitente
from app.db.models.destinatario import Destinatario
from app.db.models.transportadora import Transportadora
from app.db.models.produtos import Produtos
from app.db.models.imposto import Imposto
from app.schemas.nfe import NFeCreate


def save_nfe(db: Session, nfe_data: NFeCreate):
    existing_nfe = db.query(NFe).filter_by(chave_acesso=nfe_data.chave_acesso).first()
    if existing_nfe:
        raise ValueError(f"NF-e com chave {nfe_data.chave_acesso} já foi importada.")
    emitente = get_or_create_emitente(db, nfe_data.emitente)
    destinatario = get_or_create_destinatario(db, nfe_data.destinatario)
    transportadora = get_or_create_transportadora(db, nfe_data.transportadora)

    nfe = NFe(
        chave_acesso=nfe_data.chave_acesso,
        numero=nfe_data.numero,
        serie=nfe_data.serie,
        data_emissao=nfe_data.data_emissao,
        valor_total=nfe_data.valor_total,
        emitente_id=emitente.id,
        destinatario_id=destinatario.id,
        transportadora_id=transportadora.id
    )
    db.add(nfe)
    db.commit()
    db.refresh(nfe)

    # products + impostos
    for prod_data in nfe_data.produtos:
        produto = Produtos(
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
