from fastapi import APIRouter, HTTPException
from security.sensor_monitor import SensorMonitor

router = APIRouter()

sensor_monitor = SensorMonitor()

@router.post("/sensor/temperature")
async def update_temperature(payload: dict):
    value = payload.get("value")

    if value is None:
        raise HTTPException(status_code=400, detail="Missing sensor value")

    if sensor_monitor.inspect("temperature", value):
        raise HTTPException(
            status_code=403,
            detail="Anomalous sensor data detected"
        )

    return {"status": "accepted", "value": value}
