# simulated attacker script

import requests
import time

URL = "http://127.0.0.1:8000/auth/login"

RANDOM_IPS_POOL = [
    "127.0.0.1",
    "192.168.1.1",
    "10.14.51.73",
    "192.168.1.45",
    "243.153.64.81",
    "121.156.55.208",
    "73.79.7.134",
    "28.1.176.89",
    "183.19.217.196",
    "116.172.149.191",
    "245.15.60.109",
    "36.53.249.75",
    "14.185.63.191",
    "8.83.218.69",
    "163.47.165.75",
    "183.244.242.57",
    "68.235.148.160",
    "91.250.125.81",
    "235.82.153.232",
    "85.138.135.202",
    "82.253.131.216",
    "141.39.97.20",
    "6.76.197.179",
    "40.127.211.70"
]

payload = {
    "username": "admin",
    "password": "wrongpass"
}

for i in range((len(RANDOM_IPS_POOL))):
    fake_ip = RANDOM_IPS_POOL[i]
    headers = {
        "X-Forwarded-For": fake_ip
    }
    r = requests.post(URL, json=payload, headers=headers, timeout=2)
    print(f"{i+1}, {fake_ip}: {r.status_code} - {r.text}")
    time.sleep(0.2)

# X-Forwarded-For: it identifies the original IP address of a client connecting to a web server through a proxy, load balancer,
# or other intermediary, preventing the server from only seeing the proxy's IP