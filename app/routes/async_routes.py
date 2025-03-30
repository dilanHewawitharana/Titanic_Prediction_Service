from fastapi import APIRouter, BackgroundTasks
from uuid import uuid4
from app.model.inference import predict

router = APIRouter()
tasks = {}

def process_prediction(task_id, data):
    tasks[task_id] = predict(data["data"])

@router.post("/titanic_async")
async def titanic_async(data: dict, background_tasks: BackgroundTasks):
    task_id = str(uuid4())
    tasks[task_id] = "Processing"
    background_tasks.add_task(process_prediction, task_id, data)
    return {"task_id": task_id}

@router.get("/titanic_result/{task_id}")
async def get_result(task_id: str):
    return {"task_id": task_id, "result": tasks.get(task_id, "Not Found")}
