# endpoints

from fastapi import APIRouter, HTTPException
from security.context import firmware_monitor

router = APIRouter(prefix="/devices", tags=["Devices"])
@router.get("/")
async def list_devices():
    return {"devices": ["camera", "thermostat", "lock"]}


@router.post("/device/update")
async def firmware_update(payload: dict):
    device_id = payload.get("device_id", "unknown")

    if firmware_monitor.inspect(device_id):
        raise HTTPException(
            status_code=403,
            detail="Suspicious firmware update behavior"
        )

    return {"status": "firmware updated"}
