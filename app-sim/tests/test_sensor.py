from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_sensor_temp_normal():     
    value = 20.0
    response = client.post(
        "/sensors/temperature",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"value": value}
    )
    assert response.status_code == 200
    assert response.json() == {"status":"accepted","value":20}

def test_sensor_temp_poisoned_high():     
    value = 100.0  # Poisoned high value
    response = client.post(
        "/sensors/temperature",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"value": value}
    )
    assert response.status_code == 403
    assert response.json() == {"detail":"Anomalous sensor data detected (value: 100.0)"}

def test_sensor_temp_poisoned_low():     
    value = -100.0  # Poisoned low value
    response = client.post(
        "/sensors/temperature",
        headers={"X-Forwarded-For": "192.168.1.10"},
        json={"value": value}
    )
    assert response.status_code == 403
    assert response.json() == {"detail":"Anomalous sensor data detected (value: -100.0)"}