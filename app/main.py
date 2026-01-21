from fastapi import FastAPI
from app.routers import routes, alerts, health

app = FastAPI(title="Transport API Backend")

app.include_router(health.router)
app.include_router(routes.router)
app.include_router(alerts.router)