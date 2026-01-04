import time
from ai.anomaly_detector import AnomalyDetector

class MitMMonitor:
    """
    Detects abnormal latency & replay-like behavior
    """
    def __init__(self):
        self.latency_detector = AnomalyDetector()
        self.last_request_time = {}

    def inspect(self, client_id):
        now = time.time()

        if client_id in self.last_request_time:
            latency = now - self.last_request_time[client_id]

            if self.latency_detector.update(latency):
                print(f"[ALERT][MitM] Abnormal latency detected for {client_id}")
                return True

        self.last_request_time[client_id] = now
        return False
