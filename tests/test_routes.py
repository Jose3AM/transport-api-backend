from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_routes():
    response = client.get("/routes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_route_not_found():
    response = client.get("/routes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Route not found"