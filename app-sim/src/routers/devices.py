# endpoints

from fastapi import APIRouter

router = APIRouter(prefix="/devices", tags=["Devices"])
@router.get("/")
async def list_devices():
    return {"devices": ["camera", "thermostat", "lock"]}