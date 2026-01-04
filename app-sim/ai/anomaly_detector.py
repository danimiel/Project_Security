# so instead of block if > 5 rps/rpm, we learn normal behavior --> flag deviations
# simple AI logic to track average requests per minute and/or standard deviation
# flag anomalies using: Z-score, moving average, EWMA...

class AnomalyDetector:
    def __init__(self, window_size=5, valid_range=None):
        self.window_size = window_size
        self.valid_range = valid_range
        self.fixed_error_margin = 1.0 # simulation of error margin in physical sensors
        self.window = []

    def inspect(self, value: float) -> bool:
        is_anomaly = False
                
        # Physical range rule
        if self.valid_range:
            min_v, max_v = self.valid_range
            if value < min_v or value > max_v:
                return True

        # Warm-up phase
        if len(self.window) < self.window_size:
            self.window.append(value)
            return False

        mean = sum(self.window) / len(self.window)
        variance = sum((x - mean) ** 2 for x in self.window) / len(self.window)
        std = variance ** 0.5

        k = max(2.0, min(4.0, 2 + std / max(mean, 1e-6))) # dynamic k

        #is_anomaly = abs(value - mean) > k * std
        if ( abs(value - self.fixed_error_margin) - mean > k * std) or ( abs(value + self.fixed_error_margin) - mean > k * std):
            is_anomaly = False
            
        # FIFO update (only if it is a normal value)
        if not is_anomaly:
            self.window.pop(0)
            self.window.append(value)
            
        print(f"[DEBUG][AnomalyDetector] value={value}, mean={mean:.2f}, std={std:.2f}, k={k:.2f}, is_anomaly={is_anomaly}")

        return is_anomaly
