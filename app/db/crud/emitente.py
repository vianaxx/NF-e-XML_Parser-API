from sqlalchemy.orm import Session
from app.db.models.emitente import Emitente


def get_or_create_emitente(db: Session, emitente_data):
    instance = db.query(Emitente).filter_by(cnpj=emitente_data.cnpj).first()
    if instance:
        return instance
    instance = Emitente(**emitente_data.dict())
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
