from app.repositories.routes_repository import get_all_routes, get_route_by_id
from app.database import SessionLocal
from app.models import RouteModel

def get_all_routes(status: str | None = None,
    limit: int = 10,
    offset: int = 0
):
    db = SessionLocal()
    query = db.query(RouteModel)
    
    if status:
        query = query.filter(RouteModel.status == status)

    total = query.count()
    routes = query.offset(offset).limit(limit).all()
    db.close()
    return routes, total

def get_route_by_id(route_id: int):
    db = SessionLocal()
    route = db.query(RouteModel).filter(RouteModel.id == route_id).first()
    db.close()
    return route