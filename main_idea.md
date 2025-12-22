# 1 - Smart Home simulation (simulated IoT APIs)
## FastAPI
### simulate cameras, hubs, sensors, etc. Endpoints REST with auth. Ideal for logs and events 
```py
from fastapi import FastAPI, Depends
app = FastAPI()
```
Use for:
- /camera/stream
- /sensor/read
- /auth/login

## Pydantic
### Devide modeling, traffic validation
```py
class LoginRequest(BaseModel):
    user: str
    password: str
```

# 2 - Firewall / WAF
Firewall middleware

## Starlette Middleware (middleware firewall)
FastAPI runs on Starlette --> we can create a middleware WAF

Functions:
- Rate limiting
- IP allowlist
- Pattern detection
- Scoring by IP
  
```py
class FirewallMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        ...
```

## slowapi (Rate limiting)
- Cloudflare-like rate limiting
- IP based
- Simple
```py
from slowapi import Limiter
```

## netaddr (IP Whitelist / Blacklist)
IP range management and private networks

```py
from netaddr import IPAddress, IPNetwork
```

# 3 - Botnets / credential stuffing
## Behavioral analysis
collections / defaultdict (Error count per IP)
temporary windows

## datetime / time
Sliding windows

Conceptual example:
```py
failed_logins[ip].append(timestamp)
```

## Credential stuffing
difflib / regex (repeating pattern detection), sequential usernames
```py
import re
```

## Botnet simulation detection
scikit-learn

Doable but not necessarily needed: KMeans / IsolationForest; anomaly detection
```py
from sklearn.ensemble import IsolationForest
```

It is ideal to show defensive ML

# 4 - Reputation and IP scoring
## IP reputation system
Redis + redis-py:
- Quick datawarehouse
- IP counters
- auto TTL

```py
import redis
r.incr(ip)
```

## Defensive scoring
```py
score[ip] += weight
if score[ip] > threshold:
    block(ip)
```

# 5 - Attack simulation
## Automated traffic
Locust:
- Simulated botnets
- Credential stuffing
- API abuse

```py
class BotUser(HttpUser):
    @task
    def login(self):
        self.client.post("/login")
```

Httpx / aiohttp:
- Async traffic
- Good control
  
```py
import httpx
```

# 6 - Adversary Model modeling (MITRE-like)
## Adversary repr
Using dataclasses. Defining adversary profiles
```py
@dataclass
class Adversary:
    rate: int
    credential_attempts: int
```

## Simulación de tácticas
Repetition
IP distribution
Human vs bot timing

# 7 - Logging, metrics and visualization
## Security logs
structlog:
- structured logs
- easy analysis

## Metrics
prometheus_client:
- bloqued requests
- banned IPs
- request time

## Visualization
matplotlib / seaborn (like in the 3 assignments)

# Possible frameworks

## Orchestration
Docker + docker-compose:
- Firewall
- IoT devices
- Redis
- Locust

## Config
dynaconf:
- Firewall rules
- Umbrales
- IP lists
  


| Layer          | Software             |
| -------------- | -------------------- |
| IoT APIs       | FastAPI              |
| Firewall       | Middleware + slowapi |
| IP scoring     | Redis                |
| Bot simulation | Locust               |
| Detección      | Python + sklearn     |
| Logs           | structlog            |

# Flux
Locust (botnets)
     ↓
FastAPI Firewall Middleware
     ↓
IoT API endpoints
     ↓
Logs / Scoring / Redis

With no Docker, only VSCode:

[Traffic Simulator]
        ↓
[Python WAF / Firewall]
        ↓
[Gateway Domótico (API)]
        ↓
[IoT Devices simulados]


---

```py
pip install fastapi uvicorn slowapi scikit-learn requests loguru pydantic netaddr
```

Endpoints examples:
POST /login
GET  /camera/feed
POST /light/on
GET  /sensor/temp


### How to execute
Two steps: run firewall, and execute attacker's script

1. cd .\app-sim\
2. uvicorn src.main:app --reload
3. (in a different terminal) python attacker/attacker.py
