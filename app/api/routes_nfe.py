from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.parser_xml import parse_nfe_xml
from app.db.crud.nfe import save_nfe
from app.db.session import get_db

router = APIRouter()

@router.post("/upload", summary="Upload XML da NFe", response_model=dict)
async def upload_nfe(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".xml"):
        raise HTTPException(status_code=400, detail="Arquivo precisa ser XML")

    content = await file.read()
    try:
        nfe_data = parse_nfe_xml(content.decode("utf-8"))
        save_nfe(db, nfe_data)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

    return {"message": "Nota fiscal processada com sucesso"}