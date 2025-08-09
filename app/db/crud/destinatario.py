from sqlalchemy.orm import Session
from app.db.models.destinatario import Destinatario


def get_or_create_destinatario(db: Session, destinatario_data):
    instance = db.query(Destinatario).filter_by(cnpj=destinatario_data.cnpj).first()
    if instance:
        return instance
    instance = Destinatario(**destinatario_data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
