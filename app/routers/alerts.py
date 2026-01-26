from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.alerts_service import get_all_alerts
from app.security import verify_api_key

router = APIRouter()

@router.get("/alerts", dependencies=[Depends(verify_api_key)])
def read_alerts(db: Session = Depends(get_db)):
    return get_all_alerts(db)