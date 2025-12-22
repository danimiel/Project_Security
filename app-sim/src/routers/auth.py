# login IoT (simulated)

from fastapi import APIRouter, Request
from src.middleware.rate_limit import limiter
from src.models.schemas import LoginRequest
from src.core.logger import logger

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
@limiter.limit("5/minute")
async def login(request: Request, data: LoginRequest):
    logger.info(f"Login attempt from {request.client.host} - user={data.username}")
    return {"status": "login attempt"}