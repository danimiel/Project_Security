from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# global access control via middleware (IP filtering)

def test_list_devices_allowed_ip():
    response = client.get(
        "/devices/",
        headers={"X-Forwarded-For": "192.168.1.10"}
    )
    assert response.status_code == 200
    assert "devices" in response.json()


def test_list_devices_blocked_ip():
    response = client.get(
        "/devices/",
        headers={"X-Forwarded-For": "9.9.9.9"}
    )
    assert response.status_code == 403
