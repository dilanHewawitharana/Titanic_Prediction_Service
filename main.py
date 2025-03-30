from fastapi import FastAPI
from app.routes import sync_routes, async_routes  # Updated module name

app = FastAPI()

app.include_router(sync_routes.router)
app.include_router(async_routes.router)  # Updated reference
