import random
import requests
import time

SERVER_URL = "http://localhost:5000/receive_data"
THREAT_URL = "http://localhost:5000/report_threat"

SENSOR_TYPES = ["flooding", "public_health", "nuclear_war"]
THREAT_DESCRIPTIONS = [
    "Suspicious package detected at the tube station.",
    "Unauthorised drone activity near a government building.",
    "Cyber attack detected on the city’s infrastructure.",
    "Multiple reports of armed individuals in a public area."
]

def generate_mock_data():
    while True:
        sensor_type = random.choice(SENSOR_TYPES)
        value = round(random.uniform(0, 120), 2)  # Generate a value (some above threshold)

        data = {
            "sensor_type": sensor_type,
            "value": value
        }

        print(f"📡 Sending Sensor Data: {data}")
        requests.post(SERVER_URL, json=data)

        # Simulate a terrorist threat alert randomly
        if random.random() < 0.1:  # 10% chance of a threat alert
            threat_data = {"description": random.choice(THREAT_DESCRIPTIONS)}
            print(f"🚨 Sending Threat Alert: {threat_data}")
            requests.post(THREAT_URL, json=threat_data)

        time.sleep(random.randint(3, 7))  # Simulate varied sensor reporting intervals

if __name__ == "__main__":
    generate_mock_data()
