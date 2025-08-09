from sqlalchemy.orm import Session

from app.db.models import Entrega


def get_or_create_entrega(db: Session, entrega_data):
    instance = db.query(Entrega).filter_by(cnpj=entrega_data.cnpj).first()
    if instance:
        return instance
    instance = Entrega(**entrega_data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
