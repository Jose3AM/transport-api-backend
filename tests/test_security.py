from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_routes_without_api_key():
    response = client.get("/routes")
    assert response.status_code == 401


def test_routes_with_invalid_api_key():
    response = client.get(
        "/routes",
        headers={"X-API-Key": "wrong-key"}
    )
    assert response.status_code == 403


def test_routes_with_valid_api_key():
    response = client.get(
        "/routes",
        headers={"X-API-Key": "super-secret-key"}
    )
    assert response.status_code == 200