from app.models import Alert
from sqlalchemy.orm import Session

def get_all_alerts(db: Session):
    return db.query(Alert).all()