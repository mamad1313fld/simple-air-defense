import random
import time

class Radar:
    def __init__(self):
        self.threats = []

    def detect_threat(self):
        threat = {"id": len(self.threats) + 1, "distance": random.randint(1, 100), "speed": random.randint(1, 10)}
        self.threats.append(threat)
        return threat

class BMC:
    def __init__(self):
        self.interceptors = []

    def evaluate_threat(self, threat):
        if threat["distance"] < 50:
            self.interceptors.append(threat)
            return True
        return False

    def intercept_threat(self, threat):
        success = random.choice([True, False])
        if success:
            print(f"Threat {threat['id']} intercepted successfully!")
        else:
            print(f"Threat {threat['id']} interception failed!")

def main():
    radar = Radar()
    bmc = BMC()
    
    while True:
        threat = radar.detect_threat()
        print(f"Detected threat: {threat}")
        
        if bmc.evaluate_threat(threat):
            bmc.intercept_threat(threat)
        
        time.sleep(2)

if __name__ == "__main__":
    main()
