import time
import requests

TARGET = "http://127.0.0.1:8000/device/update"

payload = {
    "device_id": "thermostat-01"
}

def firmware_attack():
    """
    Simulates frequent or suspicious updates
    """
    for i in range(15):
        r = requests.post(TARGET, json=payload)
        print(f"[{i}] Status:", r.status_code, r.text)
        time.sleep(2)
    


if __name__ == "__main__":
    print("[*] Starting Firmware Attack simulation")
    firmware_attack()
