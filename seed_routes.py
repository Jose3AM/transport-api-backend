from app.database import SessionLocal
from app.models import RouteModel

def seed_routes():
    db = SessionLocal()

    routes = [
        RouteModel(id=1, name="Route Downtown - North", status="active"),
        RouteModel(id=2, name="Route South - Downtown", status="suspended"),
    ]

    db.add_all(routes)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_routes()