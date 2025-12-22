from fastapi import Request
from fastapi.responses import JSONResponse
from src.core.security import is_ip_allowed
from src.core.logger import logger

async def ip_whitelist_middleware(request: Request, call_next):
    client_ip = request.client.host

    if not is_ip_allowed(client_ip):
        logger.warning(f"Blocked IP: {client_ip}")
        return JSONResponse(
            status_code=403,
            content={"detail": "IP not allowed"}
        )
    logger.info(f"Allowed IP: {client_ip}")

    return await call_next(request)
