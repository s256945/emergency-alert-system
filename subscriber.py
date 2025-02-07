import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"[SUBSCRIBER] 🚨 Received Alert: {message.payload.decode()}")

# Create MQTT client
client = mqtt.Client()

# Set up the message callback
client.on_message = on_message

# Connect to the broker with a 120-second timeout to avoid connection timeout errors
client.connect(BROKER, PORT, 120)

# Subscribe to the topic
client.subscribe(TOPIC)
print(f"[SUBSCRIBER] Listening for alerts on {TOPIC}...")

# Start MQTT loop to keep listening
client.loop_forever()