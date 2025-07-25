from fastapi import FastAPI
from api.v1.api_v1 import api_router
from db.database import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="NF-e XML Parser API",
    version="1.0.0",
    description="API para importar, extrair e consultar dados de NF-e a partir de arquivos XML"
)


# Inclui todas as rotas v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "NF-e XML Parser API - Online"}



