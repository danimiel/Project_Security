from ai.anomaly_detector import AnomalyDetector
import time

class MitMMonitor:
    def __init__(self):
        self.latency_detector = AnomalyDetector(
            window_size=10,
            valid_range=(0, 2)  # seconds
        )

    def inspect(self, client_ip: str) -> bool:
        latency = time.time() % 3  # simulated latency

        if self.latency_detector.inspect(latency):
            print(f"[ALERT][MITM] Suspicious latency from {client_ip}: {latency:.2f}s")
            return True

        return False
