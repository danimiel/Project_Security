from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_firmware_update_ok():
    response = client.post(
        "/devices/update",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"version": "2.0"}
    )
    assert response.status_code == 200
    assert response.json() == {"status":"firmware updated"}

def test_firmware_update_suspicious():
    headers = {"X-Forwarded-For": "192.168.1.20"}
    payload = {"version": "2.0"}
    last_response = None
    for _ in range(3):
        last_response = client.post(
            "/devices/update",
            headers=headers,
            json=payload
        )
        
    assert last_response.status_code == 403
    assert last_response.json() == {"detail":"Suspicious firmware update behavior"}