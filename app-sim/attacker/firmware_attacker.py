from random import uniform
import time
import requests

TARGET = "http://127.0.0.1:8000/devices/update"

payload = {
    "device_id": "thermostat-01"
}

def firmware_attack():
    """
    Simulates frequent or suspicious updates
    """
    for i in range(10):
        r = requests.post(TARGET, json=payload)
        print(f"[{i+1}] Status:", r.status_code, r.text)
        t = uniform(0.1, 1.0)
        time.sleep(t)
    

if __name__ == "__main__":
    print("[*] Starting Firmware Attack simulation")
    firmware_attack()
