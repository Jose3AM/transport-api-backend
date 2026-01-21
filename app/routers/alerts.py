from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.alerts_service import get_all_alerts

router = APIRouter()

@router.get("/alerts")
def read_alerts(db: Session = Depends(get_db)):
    return get_all_alerts(db)