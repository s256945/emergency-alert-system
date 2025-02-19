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

if choice == '1':
    alert_message = (
        f"🚨 Flooding Alert! 🚨\n"
        f"📍 Location: Ipswich town centre, Suffolk\n"
        f"🕒 Time: Immediate\n"
        f"❗ Implications: Potential for severe property damage and risk to life.\n"
        f"🏥 Health & Welfare: Move to higher ground, avoid walking or driving through floodwaters.\n"
        f"📢 Advice: Follow evacuation orders and stay tuned to local news for updates.\n"
        f"🛡️ Reassurance: Emergency services are responding. Stay calm and stay safe.\n"
        f"🔌 Practical Implications: Expect disruptions to traffic, power supplies, telephones, and water supplies.\n"
        f"📞 Helpline: For assistance, call the Suffolk emergency helpline at 0345 606 6067.\n"
        f"👤 Published by: {name}"
    )
    topic = "emergency/flooding"
elif choice == '2':
    alert_message = (
        f"🚨 Terrorist Threat Alert! 🚨\n"
        f"📍 Location: Colchester, Essex\n"
        f"🕒 Time: Immediate\n"
        f"❗ Implications: Potential for severe injury and loss of life.\n"
        f"🏥 Health & Welfare: Avoid the area, stay indoors, and follow instructions from authorities.\n"
        f"📢 Advice: Report any suspicious activity to the police immediately. Do not spread rumors.\n"
        f"🛡️ Reassurance: Law enforcement is actively responding. Stay vigilant and stay safe.\n"
        f"🚇 Practical Implications: Expect heightened security measures and possible disruptions to public transport.\n"
        f"📞 Helpline: For assistance, call the Essex emergency helpline at 0345 603 7630.\n"
        f"👤 Published by: {name}"
    )
    topic = "emergency/terrorist_threat"
elif choice == '3':
    alert_message = (
        f"🚨 Public Health Emergency Alert! 🚨\n"
        f"📍 Location: Chelmsford, Essex\n"
        f"🕒 Time: Immediate\n"
        f"❗ Implications: Potential for widespread illness and health complications.\n"
        f"🏥 Health & Welfare: Follow health guidelines, wear masks, and maintain social distancing.\n"
        f"📢 Advice: Avoid large gatherings, wash hands frequently, and stay informed through official channels.\n"
        f"🛡️ Reassurance: Health authorities are managing the situation. Stay informed and stay safe.\n"
        f"🔌 Practical Implications: Expect disruptions to public services and healthcare facilities.\n"
        f"📞 Helpline: For assistance, call the Essex health emergency helpline at 0300 303 9988.\n"
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
