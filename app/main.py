from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from app.data import routes, alerts
from app.schemas import Route, Alert
from typing import List

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/routes", status_code=status.HTTP_200_OK, response_model=List[Route])
def get_routes():
    return routes if routes else []

@app.get("/alerts", status_code=status.HTTP_200_OK, response_model=List[Alert])
def get_alerts():
    return alerts if alerts else []

@app.get("/routes/{route_id}")
def get_route_by_id(route_id: int):
    for route in routes:
        if route["id"] == route_id:
            return route
    raise HTTPException(
        status_code=404,
        detail="Route not found"
    )