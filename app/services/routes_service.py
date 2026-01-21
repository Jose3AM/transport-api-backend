from app.repositories.routes_repository import get_all_routes, get_route_by_id
from app.database import SessionLocal
from app.models import RouteModel

def fetch_routes():
    return get_all_routes()

def fetch_route_by_id(route_id: int):
    return get_route_by_id(route_id)

def get_all_routes(status: str | None = None):
    db = SessionLocal()
    query = db.query(RouteModel)
    
    if status:
        query = query.filter(RouteModel.status == status)

    routes = query.all()
    db.close()
    return routes


def get_route_by_id(route_id: int):
    db = SessionLocal()
    route = db.query(RouteModel).filter(RouteModel.id == route_id).first()
    db.close()
    return route