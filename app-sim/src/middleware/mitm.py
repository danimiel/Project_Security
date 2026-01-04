from fastapi import Request
from security.context import mitm_monitor

async def mitm_middleware(request: Request, call_next):
    client_ip = request.client.host
    mitm_monitor.inspect(client_ip)
    response = await call_next(request)
    return response
