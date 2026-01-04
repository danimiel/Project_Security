import time
from ai.anomaly_detector import AnomalyDetector

class FirmwareMonitor:
    """
    Detects abnormal update frequency
    """
    def __init__(self):
        self.update_detector = AnomalyDetector()
        self.last_update = {}

    def inspect(self, device_id):
        now = time.time()

        if device_id in self.last_update:
            interval = now - self.last_update[device_id]

            if self.update_detector.update(interval):
                print(f"[ALERT][Firmware] Abnormal update behavior on {device_id}")
                return True

        self.last_update[device_id] = now
        return False
