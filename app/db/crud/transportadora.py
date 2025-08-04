from sqlalchemy.orm import Session
from app.db.models.transportadora import Transportadora


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
