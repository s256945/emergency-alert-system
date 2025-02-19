import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC

# Create MQTT client
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Publish a flooding alert
flooding_alert_message = (
    "🚨 Flooding Alert! 🚨\n"
    "📍 Location: Ipswich town centre, Suffolk\n"
    "🕒 Time: Immediate\n"
    "❗ Implications: Potential for severe property damage and risk to life.\n"
    "🏥 Health & Welfare: Move to higher ground, avoid walking or driving through floodwaters.\n"
    "📢 Advice: Follow evacuation orders and stay tuned to local news for updates.\n"
    "🛡️ Reassurance: Emergency services are responding. Stay calm and stay safe.\n"
    "🔌 Practical Implications: Expect disruptions to traffic, power supplies, telephones, and water supplies.\n"
    "📞 Helpline: For assistance, call the emergency helpline at 123-456-7890."
)
client.publish("emergency/flooding", flooding_alert_message)
print(f"[PUBLISHER] Sent alert: {flooding_alert_message}")

# Publish a terrorist threat alert
terrorist_threat_alert_message = (
    "🚨 Terrorist Threat Alert! 🚨\n"
    "📍 Location: Colchester, Essex\n"
    "🕒 Time: Immediate\n"
    "❗ Implications: Potential for severe injury and loss of life.\n"
    "🏥 Health & Welfare: Avoid the area, stay indoors, and follow instructions from authorities.\n"
    "📢 Advice: Report any suspicious activity to the police immediately. Do not spread rumors.\n"
    "🛡️ Reassurance: Law enforcement is actively responding. Stay vigilant and stay safe.\n"
    "🚇 Practical Implications: Expect heightened security measures and possible disruptions to public transport.\n"
    "📞 Helpline: For assistance, call the emergency helpline at 123-456-7890."
)
client.publish("emergency/terrorist_threat", terrorist_threat_alert_message)
print(f"[PUBLISHER] Sent alert: {terrorist_threat_alert_message}")

# Publish a public health emergency alert
public_health_emergency_alert_message = (
    "🚨 Public Health Emergency Alert! 🚨\n"
    "📍 Location: Chelmsford, Essex\n"
    "🕒 Time: Immediate\n"
    "❗ Implications: Potential for widespread illness and health complications.\n"
    "🏥 Health & Welfare: Follow health guidelines, wear masks, and maintain social distancing.\n"
    "📢 Advice: Avoid large gatherings, wash hands frequently, and stay informed through official channels.\n"
    "🛡️ Reassurance: Health authorities are managing the situation. Stay informed and stay safe.\n"
    "🔌 Practical Implications: Expect disruptions to public services and healthcare facilities.\n"
    "📞 Helpline: For assistance, call the health emergency helpline at 987-654-3210."
)
client.publish("emergency/public_health", public_health_emergency_alert_message)
print(f"[PUBLISHER] Sent alert: {public_health_emergency_alert_message}")

# Disconnect
client.disconnect()
