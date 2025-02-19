import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC

# Create MQTT client
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# User enters their name
name = input("Enter your name: ")

# User selects which alert to send
print(f"Hello, {name}! Select which alert to send:")
print("1. Flooding Alert")
print("2. Terrorist Threat Alert")
print("3. Public Health Alert")
choice = input("Enter your choice (1/2/3): ")

# User enters the details of the alert
location = input("📍 Enter the location of the event: ")
time = input("🕒 Enter the time of the event: ")
implications = input("❗ Enter the implications of the event: ")
healthWelfareInfo = input("🏥 Enter the health and welfare advice: ")
advice = input("📢 Enter the advice/instructions to follow: ")
reassurance = input("🛡️ Enter the reassurance: ")
implications = input("🔌 Enter the practical implications that may be faced: ")
helpline = input("📞 Enter the helplines/emergency numbers to call: ")

if choice == '1':
    alert_message = (
        f"🚨🌊 Flooding Alert! 🌊🚨\n"
        f"📍 Location: {location}\n"
        f"🕒 Time: {time}\n"
        f"❗ Implications: {implications}\n"
        f"🏥 Health & Welfare: {healthWelfareInfo}\n"
        f"📢 Advice: {advice}\n"
        f"🛡️ Reassurance: {reassurance}\n"
        f"🔌 Practical Implications: {implications}\n"
        f"📞 Helpline: {helpline}\n"
        f"👤 Published by: {name}"
    )
    topic = "emergency/flooding"
elif choice == '2':
    alert_message = (
        f"🚨💥 Terrorist Threat Alert! 💥🚨\n"
        f"📍 Location: {location}\n"
        f"🕒 Time: {time}\n"
        f"❗ Implications: {implications}\n"
        f"🏥 Health & Welfare: {healthWelfareInfo}\n"
        f"📢 Advice: {advice}\n"
        f"🛡️ Reassurance: {reassurance}\n"
        f"🔌 Practical Implications: {implications}\n"
        f"📞 Helpline: {helpline}\n"
        f"👤 Published by: {name}"
    )
    topic = "emergency/terrorist_threat"
elif choice == '3':
    alert_message = (
        f"🚨🦠 Public Health Emergency Alert! 🦠🚨\n"
        f"📍 Location: {location}\n"
        f"🕒 Time: {time}\n"
        f"❗ Implications: {implications}\n"
        f"🏥 Health & Welfare: {healthWelfareInfo}\n"
        f"📢 Advice: {advice}\n"
        f"🛡️ Reassurance: {reassurance}\n"
        f"🔌 Practical Implications: {implications}\n"
        f"📞 Helpline: {helpline}\n"
        f"👤 Published by: {name}"
    )
    topic = "emergency/public_health"
else:
    print("Invalid choice. Exiting.")
    exit()

client.publish(topic, alert_message)
print(f"[{name}] Sent alert: {alert_message}")

# Disconnect
client.disconnect()
