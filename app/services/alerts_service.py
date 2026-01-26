from app.models import AlertModel
from sqlalchemy.orm import Session

def get_all_alerts(db: Session):
    return db.query(AlertModel).all()