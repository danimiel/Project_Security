from ai.anomaly_detector import AnomalyDetector

class SensorMonitor:
    """
    Detects sensor poisoning using AI-based anomaly detection
    """

    def __init__(self):
        self.detectors = {
            "temperature": AnomalyDetector(valid_range=(15, 30)),
            "humidity": AnomalyDetector(valid_range=(30, 70)),
        }

    def inspect(self, sensor_type: str, value: float) -> bool:
        detector = self.detectors.get(sensor_type)

        # Unknown sensor --> ignore
        if not detector:
            return False

        # AI decision
        is_anomaly = detector.inspect(value)

        if is_anomaly:
            print(f"[ALERT][Sensor] Anomalous {sensor_type} value: {value}")
            return True

        return False
