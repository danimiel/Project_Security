from fastapi import FastAPI, Request
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from src.middleware.ip_filter import ip_whitelist_middleware
from src.middleware.rate_limit import limiter
from src.middleware.mitm import mitm_middleware
from src.routers import auth, devices
from src.routers.sensor import router as sensor_router
from src.core.logger import logger


"""from security.mitm_monitor import MitMMonitor
from security.sensor_monitor import SensorMonitor
from security.firmware_monitor import FirmwareMonitor"""

logger.info("Starting application...")

app = FastAPI(title="IoT Device Management API", version="1.2.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.middleware("http")(ip_whitelist_middleware)

app.include_router(auth.router)
app.include_router(devices.router)
app.middleware("http")(mitm_middleware)
app.include_router(sensor_router)



"""mitm_monitor = MitMMonitor()
sensor_monitor = SensorMonitor()
firmware_monitor = FirmwareMonitor()

mitm_monitor.inspect(client_id)
sensor_monitor.inspect("temperature", value)
firmware_monitor.inspect(device_id)"""