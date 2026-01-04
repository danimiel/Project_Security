# so instead of block if > 10 requests per second, we learn normal behavior --> flag deviations
# simple AI logic to track average requests per minute and/or standard deviation
# flag anomalies using: Z-score, moving average, EWMA...

# ai/anomaly_detector.py

class AnomalyDetector:
    def __init__(self, window_size=20, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.history = []

    def update(self, value):
        self.history.append(value)

        if len(self.history) > self.window_size:
            self.history.pop(0)

        if len(self.history) < self.window_size:
            return False

        mean = sum(self.history) / len(self.history)
        variance = sum((x - mean) ** 2 for x in self.history) / len(self.history)
        std = variance ** 0.5

        return abs(value - mean) > self.threshold * std
