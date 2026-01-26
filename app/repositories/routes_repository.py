from app.data import routes

def get_all_routes():
    return routes

def get_route_by_id(route_id: int):
    for route in routes:
        if route["id"] == route_id:
            return route
    return None
