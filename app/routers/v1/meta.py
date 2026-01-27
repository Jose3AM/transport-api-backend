from fastapi import APIRouter
from app.utils.responses import success_response

router = APIRouter(
    tags=["Meta"]
)

@router.get("/meta")
def get_meta():
    return success_response({
        "project_name": "Transport API Backend",
        "version": "1.0.0",
        "status": "active",
    })