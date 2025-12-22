from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from src.middleware.ip_filter import ip_whitelist_middleware
from src.middleware.rate_limit import limiter
from src.routers import auth, devices
from src.core.logger import logger

logger.info("Starting application...")

app = FastAPI(title="IoT Device Management API", version="1.2.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.middleware("http")(ip_whitelist_middleware)

app.include_router(auth.router)
app.include_router(devices.router)