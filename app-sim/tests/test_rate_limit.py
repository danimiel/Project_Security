from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# simulates brute-force login attempts to test rate limiting (SlowAPI working)

def test_rate_limit_exceeded():
    headers = {"X-Forwarded-For": "192.168.1.20"}
    payload = {"username": "test", "password": "test"}

    last_response = None
    for _ in range(6):
        last_response = client.post("/auth/login", headers=headers, json=payload)

    assert last_response.status_code == 429
