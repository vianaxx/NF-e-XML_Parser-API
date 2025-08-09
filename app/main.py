from fastapi import FastAPI
from app.api.routes_nfe import router as nfe_router
from app.db.base import Base
from app.db.session import engine
from app.db import models

# Agora sim cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NFe XML Parser API")


@app.get("/")
def root():
    return {"msg": "NFe XML Parser API rodando"}


app.include_router(nfe_router, prefix="/api/nfe", tags=["Notas Fiscais"])
