from fastapi import APIRouter, HTTPException, Depends, Query
from app.services.routes_service import get_all_routes, get_route_by_id
from app.errors import ROUTE_NOT_FOUND, INVALID_STATUS_VALUE
from app.security import verify_api_key
from app.utils.responses import success_response

router = APIRouter(
    prefix="/routes",
    tags=["Routes"]
)

VALID_STATUSES = {"active", "suspended"}


@router.get("", dependencies=[Depends(verify_api_key)])
def get_routes(
    status: str | None = None,
    limit: int = Query(10, ge=1, le=50),
    offset: int = Query(0, ge=0)
    ):
    if status and status not in VALID_STATUSES:
        raise HTTPException(
            status_code=422,
            detail=INVALID_STATUS_VALUE
        )
    routes, total = get_all_routes(status, limit, offset)
    return success_response(
        data=routes,
        total=total,
        limit=limit,
        offset=offset
    )


@router.get("/{route_id}", dependencies=[Depends(verify_api_key)])
def get_route(route_id: int):
    route = get_route_by_id(route_id)
    if not route:
        raise HTTPException(
            status_code=404,
            detail=ROUTE_NOT_FOUND
        )
    return route