from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import logging
from config import BROKER, PORT
from alerts import ALERT_TEMPLATES

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# MQTT Setup with Reconnection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected to MQTT broker")
    else:
        logging.error(f"Failed to connect, return code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

# Thresholds for different sensor-based alerts
THRESHOLDS = {
    "flooding": 80,
    "nuclear_war": 50,
    "public_health": 500
}

def send_alert(sensor_type, description, location="Unknown Location"):
    alert_info = ALERT_TEMPLATES.get(sensor_type, {})
    
    alert_message = f"{alert_info.get('title', '🚨 Alert! 🚨')}\nLocation: {location}\nDetails: {description}"
    instructions = "\n".join(alert_info.get("instructions", []))
    
    full_message = f"{alert_message}\n\n📢 Instructions:\n{instructions}"
    topic = f"emergency/{sensor_type}"

    logging.info(f"Publishing alert to {topic}: {full_message}")
    client.publish(topic, full_message)

    return full_message

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    sensor_type = data.get("sensor_type")
    value = data.get("value")
    location = data.get("location", "Unknown Location")  # Default if missing

    # Data validation
    if not sensor_type or value is None:
        return jsonify({"error": "Invalid data format"}), 400
    if not isinstance(value, (int, float)):
        return jsonify({"error": "Value must be a number"}), 400
    if sensor_type not in THRESHOLDS:
        return jsonify({"error": "Invalid sensor type"}), 400

    threshold = THRESHOLDS[sensor_type]

    # Trigger alert if threshold is met
    if value >= threshold:
        message = send_alert(sensor_type, f"Level: {value}%", location)
        return jsonify({"status": "Alert triggered", "message": message}), 200

    return jsonify({"status": "Data processed, no alert needed"}), 200

@app.route('/report_threat', methods=['POST'])
def report_threat():
    data = request.json
    description = data.get("description", "No details provided")
    location = data.get("location", "Unknown Location")  # Default if missing

    message = send_alert("terrorist_threat", description, location)
    return jsonify({"status": "Threat alert sent", "message": message}), 200

if __name__ == '__main__':
    app.run(port=5005)
