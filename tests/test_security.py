from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
API_V1_STR = "/api/v1"

def test_routes_without_api_key():
    response = client.get(f"{API_V1_STR}/routes")
    assert response.status_code == 401


def test_routes_with_invalid_api_key():
    response = client.get(
        f"{API_V1_STR}/routes",
        headers={"X-API-Key": "wrong-key"}
    )
    assert response.status_code == 403


def test_routes_with_valid_api_key():
    response = client.get(
        f"{API_V1_STR}/routes",
        headers={"X-API-Key": "super-secret-key"}
    )
    assert response.status_code == 200