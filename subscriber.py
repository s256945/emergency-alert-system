import paho.mqtt.client as mqtt
from config import BROKER, PORT

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"[{userdata}] 🚨 Received Alert: {message.payload.decode()}")

# Function to create and configure a client
def create_client(alert_name, topic):
    client = mqtt.Client(userdata=alert_name)
    client.on_message = on_message
    client.connect(BROKER, PORT, 120)
    client.subscribe(topic)
    client.loop_start()
    print(f"[{alert_name}] Listening for {alert_name} alerts on '{topic}'...")
    return client

# User selects which alert to listen for
def start_subscriber():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Select which alert to subscribe to:")
    print("1. Flooding Alert")
    print("2. Terrorist Threat Alert")
    print("3. Public Health Alert")
    print("4. Nuclear War Alert")
    
    choice = input("Enter your choice (1/2/3/4): ")

    # Mapping of choices to alert types and topics
    alerts = {
        '1': ("Flooding Subscriber", "emergency/flooding"),
        '2': ("Terrorist Threat Subscriber", "emergency/terrorist_threat"),
        '3': ("Public Health Subscriber", "emergency/public_health"),
        '4': ("Nuclear War Subscriber", "emergency/nuclear_war")
    }
    
    # If user enters a valid choice, create and subscribe to the appropriate alert
    if choice in alerts:
        alert_name, topic = alerts[choice]
        client = create_client(alert_name, topic)
        client.user_data_set(name)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        return start_subscriber()  # Recursively retry if invalid choice

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
        client.disconnect()

# Start the subscriber based on user input
start_subscriber()
