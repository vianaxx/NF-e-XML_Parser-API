from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.parser import parse_nfe_xml
from db.crud.nfe import save_nfe
from schemas.nfe import NFeCreate

router = APIRouter()


@router.post("/upload")
async def upload_nfe(file: UploadFile = File(...), db: Session = Depends(get_db)):
    xml_str = await file.read()
    try:
        parsed_data = parse_nfe_xml(xml_str.decode())
        nfe_create = NFeCreate(**parsed_data)
        saved_nfe = save_nfe(db, nfe_create)
        return {"message": "NF-e salva com sucesso", "id": saved_nfe.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
