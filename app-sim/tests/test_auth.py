from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# tests scheme authentication functionality (FastAPI + Pydantic)

def test_login_success():
    response = client.post(
        "/auth/login",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"username": "admin", "password": "admin"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "login successful"


def test_login_missing_fields():
    response = client.post(
        "/auth/login",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"username": "admin"} # missing password
    )
    assert response.status_code == 422
