import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC

# Create MQTT client
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Publish an emergency alert
alert_message = "🚨 Earthquake Alert! Take cover immediately."
client.publish(TOPIC, alert_message)
print(f"[PUBLISHER] Sent alert: {alert_message}")

# Disconnect
client.disconnect()