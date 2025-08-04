from sqlalchemy.orm import Session
from app.db.models.produtos import Produtos


def get_or_create_produto(db: Session, product_data):
    instance = db.query(Produtos).filter_by(codigo=product_data.codigo).first()
    if instance:
        return instance
    instance = Produtos(
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
