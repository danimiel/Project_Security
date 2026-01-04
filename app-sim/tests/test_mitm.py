from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_allowed_ip():
    response = client.post(
        "/auth/login",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 200

def test_blocked_ip():
    response = client.post(
        "/auth/login",
        headers={"X-Forwarded-For": "8.8.8.8"},
        json={"username": "testuser", "password": "testpass"}
    )
    assert response.status_code == 403
    assert response.json()["detail"] == "IP not allowed"

def test_rate_limit_exceeded():
    headers = {"X-Forwarded-For": "192.168.1.20"}
    payload = {"username": "test", "password": "test"}

    last_response = None
    for _ in range(6):
        last_response = client.post("/auth/login", headers=headers, json=payload)

    assert last_response.status_code == 429
