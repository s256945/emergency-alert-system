import paho.mqtt.client as mqtt
from config import BROKER, PORT

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"[{userdata}] 🚨 Received Alert: {message.payload.decode()}")

# Create MQTT clients for each subscriber
client_flooding = mqtt.Client(userdata="Flooding Subscriber")
client_terrorist = mqtt.Client(userdata="Terrorist Threat Subscriber")
client_health = mqtt.Client(userdata="Public Health Subscriber")

# Set up message callback for each client
client_flooding.on_message = on_message
client_terrorist.on_message = on_message
client_health.on_message = on_message

# Connect to the brokers with a 120-second timeout
client_flooding.connect(BROKER, PORT, 120)
client_terrorist.connect(BROKER, PORT, 120)
client_health.connect(BROKER, PORT, 120)

# User selects which alert to listen for
def start_subscriber():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Select which alert to subscribe to:")
    print("1. Flooding Alert")
    print("2. Terrorist Threat Alert")
    print("3. Public Health Alert")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        client_flooding.user_data_set(name)
        client_flooding.subscribe("emergency/flooding")
        print(f"[{name}] Listening for flooding alerts on 'emergency/flooding'...")
        client_flooding.loop_start()
    elif choice == '2':
        client_terrorist.user_data_set(name)
        client_terrorist.subscribe("emergency/terrorist_threat")
        print(f"[{name}] Listening for terrorist threat alerts on 'emergency/terrorist_threat'...")
        client_terrorist.loop_start()
    elif choice == '3':
        client_health.user_data_set(name)
        client_health.subscribe("emergency/public_health")
        print(f"[{name}] Listening for public health alerts on 'emergency/public_health'...")
        client_health.loop_start()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    # Keep the main thread running
    try:
        while True:
            client_flooding.loop_forever()
            client_terrorist.loop_forever()
            client_health.loop_forever()
    except KeyboardInterrupt:
        print("Exiting...")
        client_flooding.disconnect()
        client_terrorist.disconnect()
        client_health.disconnect()

# Start the subscriber based on user input
start_subscriber()
