# so instead of block if > 5 rps/rpm, we learn normal behavior --> flag deviations
# simple AI logic to track average requests per minute and/or standard deviation
# flag anomalies using: Z-score, moving average, EWMA...

from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=5, confirm_k=2, valid_range=None):
        self.window_size = window_size
        self.confirm_k = confirm_k
        self.valid_range = valid_range

        self.window = []
        self.recent_flags = deque(maxlen=window_size)

    def inspect(self, value: float) -> bool:
        # Physical check
        if self.valid_range:
            min_v, max_v = self.valid_range
            if value < min_v or value > max_v:
                self.recent_flags.append(True)
                return True

        if len(self.window) < self.window_size:
            self.window.append(value)
            self.recent_flags.append(False)
            return False

        mean = sum(self.window) / len(self.window)
        std = (sum((x - mean) ** 2 for x in self.window) / len(self.window)) ** 0.5

        k = 2.5
        is_anomaly = abs(value - mean) > k * std

        self.recent_flags.append(is_anomaly)

        # Only confirm anomaly if enough recent flags
        confirmed = sum(self.recent_flags) >= self.confirm_k

        if not confirmed:
            self.window.pop(0)
            self.window.append(value)

        return confirmed
