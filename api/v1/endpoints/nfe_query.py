from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from db.crud.nfe import get_nfe_by_chave
from schemas.nfe import NFe

router = APIRouter()


@router.get("/{chave_acesso}", response_model=NFe)
def get_nfe(chave_acesso: str, db: Session = Depends(get_db)):
    nfe = get_nfe_by_chave(db, chave_acesso)
    if not nfe:
        raise HTTPException(status_code=404, detail="NF-e não encontrada")
    return nfe
