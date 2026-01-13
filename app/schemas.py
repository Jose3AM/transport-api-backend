from pydantic import BaseModel

class Route(BaseModel):
    id: int
    name: str
    status: str

class Alert(BaseModel):
    id: int
    route_id: int
    message: str