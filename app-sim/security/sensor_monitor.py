from ai.anomaly_detector import AnomalyDetector

class SensorMonitor:
    """
    Detects impossible or abnormal sensor values
    """
    def __init__(self):
        self.detectors = {
            "temperature": AnomalyDetector(),
            "humidity": AnomalyDetector()
        }

    def inspect(self, sensor_type, value):
        detector = self.detectors.get(sensor_type)

        if not detector:
            return False

        if detector.update(value):
            print(f"[ALERT][Sensor] Anomalous {sensor_type} value: {value}")
            return True

        return False
