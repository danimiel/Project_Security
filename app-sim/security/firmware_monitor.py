import time
from ai.anomaly_detector import AnomalyDetector

from collections import defaultdict

class FirmwareMonitor:
    def __init__(self):
        self.update_count = defaultdict(int)
        self.last_reset = time.time()
        self.window = 10          # seconds
        self.threshold = 2        # updates per device per window

    def inspect(self, device_id: str) -> bool:
        now = time.time()

        # Reset counters every window
        if now - self.last_reset > self.window:
            self.update_count.clear()
            self.last_reset = now

        self.update_count[device_id] += 1

        print(f"[FIRMWARE] {device_id}count={self.update_count[device_id]}")

        if self.update_count[device_id] > self.threshold:
            print("[ALERT] Firmware abuse detected:", device_id)
            return True

        return False
