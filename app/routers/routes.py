from fastapi import APIRouter, HTTPException, status
from app.services.routes_service import get_all_routes, get_route_by_id
from app.errors import ROUTE_NOT_FOUND, INVALID_STATUS_VALUE

router = APIRouter(
    prefix="/routes",
    tags=["routes"]
)


@router.get("")
def get_routes(status: str | None = None):
    if status and status not in ["active", "suspended"]:
        raise HTTPException(
            status_code=422,
            detail=INVALID_STATUS_VALUE
        )
    return get_all_routes(status)


@router.get("/{route_id}")
def get_route(route_id: int):
    route = get_route_by_id(route_id)
    if not route:
        raise HTTPException(
            status_code=404,
            detail=ROUTE_NOT_FOUND
        )
    return route