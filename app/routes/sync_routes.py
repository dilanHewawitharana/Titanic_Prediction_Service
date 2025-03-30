from fastapi import APIRouter
from app.model.inference import predict

router = APIRouter()

@router.post("/titanic_sync")
def titanic_sync(data: dict):
    result = predict(data["data"])
    return result
