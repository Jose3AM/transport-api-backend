from fastapi import FastAPI, HTTPException
from app.routers.v1 import routes, alerts, meta
from app.routers import health
from app.error_handlers import (
    http_exception_handler,
    general_exception_handler
)

app = FastAPI(title="Transport API Backend")

app.include_router(health.router)
app.include_router(routes.router, prefix="/api/v1")
app.include_router(alerts.router, prefix="/api/v1")
app.include_router(meta.router, prefix="/api/v1")

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)