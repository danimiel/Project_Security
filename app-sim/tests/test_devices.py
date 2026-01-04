from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

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


def test_devices_list_devices():
    response = client.get("/devices/", headers={"X-Forwarded-For": "192.168.1.10"})
    assert response.status_code == 200
    assert response.json() == {"devices": ["camera", "thermostat", "lock"]}
    
    
def test_devices_update_firmware():
    payload = {"device_id": "camera_123"}
    response = client.post("/devices/update", json=payload, headers={"X-Forwarded-For": "127.0.0.1"})
    assert response.status_code == 200
