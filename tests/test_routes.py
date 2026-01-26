from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
HEADERS = {"X-API-Key": "super-secret-key"}

def test_get_routes():
    response = client.get("/routes", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["data"]["status"] == "ok"

def test_get_route_not_found():
    response = client.get("/routes/999", headers=HEADERS)
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert "status_code" in data

def test_filter_routes_by_active_status():
    response = client.get("/routes?status=active", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)

def test_filter_routes_by_suspended_status():
    response = client.get("/routes?status=suspended", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["data"], list)

def test_filter_routes_by_unprocessed_status():
    response = client.get("/routes?status=activa", headers=HEADERS)
    assert response.status_code == 422
    assert isinstance(response.json(), dict)

def test_routes_response_structure():
    response = client.get("/routes", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert {"total", "limit", "offset", "data"} <= data.keys()
    assert isinstance(data["data"], list)


def test_routes_limit():
    response = client.get("/routes?limit=1", headers=HEADERS)
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1


def test_routes_offset_changes_results():
    first_page = client.get("/routes?limit=2&offset=0", headers=HEADERS).json()["data"]
    second_page = client.get("/routes?limit=2&offset=2", headers=HEADERS).json()["data"]
    assert first_page != second_page


def test_routes_filter_by_status():
    response = client.get("/routes?status=active", headers=HEADERS)
    assert response.status_code == 200
    assert all(route["status"] == "active" for route in response.json()["data"])