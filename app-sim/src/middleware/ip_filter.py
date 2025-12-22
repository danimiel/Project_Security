from fastapi import Request
from fastapi.responses import JSONResponse
from src.core.security import is_ip_allowed
from src.core.logger import logger

async def ip_whitelist_middleware(request: Request, call_next):
    # cloudflare-like
    ip = request.headers.get("X-Forwarded-For") or request.client.host

    if not is_ip_allowed(ip):
        logger.warning(f"Blocked IP: {ip}")
        return JSONResponse(
            status_code=403,
            content={"detail": "IP not allowed"}
        )
    logger.info(f"Allowed IP: {ip}")

    return await call_next(request)
