from fastapi import APIRouter
from api.v1.endpoints import nfe_upload, nfe_query

api_router = APIRouter()
api_router.include_router(nfe_upload.router, prefix="/nfe", tags=["NF-e"])
api_router.include_router(nfe_query.router, prefix="/nfe", tags=["NF-e"])
