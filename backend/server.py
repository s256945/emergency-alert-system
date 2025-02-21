from flask import Flask, request
import paho.mqtt.client as mqtt
from config import BROKER, PORT

app = Flask(__name__)

# MQTT Setup
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Thresholds for different sensor-based alerts
THRESHOLDS = {
    "flooding": 80,  # If water level exceeds 80%, trigger alert
    "nuclear_war": 50,  # If radiation level exceeds 50%, trigger alert
    "public_health": 500  # If virus spread exceeds 500 cases, trigger alert
}

@app.route('/receive_data', methods=['POST'])
def receive_data():
    """
    Receives sensor data and triggers alerts if thresholds are exceeded.
    """
    data = request.json
    sensor_type = data.get("sensor_type")
    value = data.get("value")

    if not sensor_type or value is None:
        return {"error": "Invalid data format"}, 400

    if sensor_type in THRESHOLDS and value >= THRESHOLDS[sensor_type]:
        alert_message = f"🚨 {sensor_type.capitalize()} Alert! 🚨\nLevel: {value}%"
        topic = f"emergency/{sensor_type}"
        client.publish(topic, alert_message)
        print(f"Alert Sent on {topic}: {alert_message}")
        return {"status": "Alert triggered", "message": alert_message}, 200

    return {"status": "Data processed, no alert needed"}, 200

if __name__ == '__main__':
    app.run(port=5000)
