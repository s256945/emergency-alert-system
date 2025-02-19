import paho.mqtt.client as mqtt
from config import BROKER, PORT
from example_alerts import ALERT_TEMPLATES

# Create MQTT client
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# User enters their name
name = input("Enter your name: ")

# User selects which alert to send
print("-" * 50)
print(f"Hello, {name}! Select which alert to send:")
for i, value in enumerate(ALERT_TEMPLATES):
    print(f"{i + 1}. {value['title']}")
print("-" * 50)

choice = input("Enter your choice (1/2/3/4): ")

# Validate choice
if not choice.isdigit() or not (1 <= int(choice) <= len(ALERT_TEMPLATES)):
    print("Invalid choice. Exiting.")
    exit()

# Get the selected alert template
alert_info = ALERT_TEMPLATES[int(choice) - 1]
print("-" * 50)
print(f"\nExample of {alert_info['title']}:")
for field, example in alert_info['sample_data'].items():
    print(f"{field}: {example}")
print(("-" * 50) + "\n")

# User enters the details of the alert
alert_details = {}
for field in alert_info['sample_data']:
    alert_details[field] = input(f"Enter the {field}: ")

alert_message = (
    ("-" * 50) + "\n" + f"🚨{alert_info['title']}🚨\n"
    + "\n".join([f"{field}: {alert_details[field]}" for field in alert_info['sample_data']]) + "\n"
    + f"👤 Published by: {name}" + "\n" + ("-" * 50)
)

# Publish the alert message to MQTT broker
client.publish(alert_info['topic'], alert_message)
print("\n" + f"[{name}] Sent alert: " + "\n" + f"{alert_message}")

# Disconnect
client.disconnect()
