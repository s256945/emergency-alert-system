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

# Display example info based on choice
if choice == '1':
    print("\nExample of Flooding Alert:")
    print("🚨🌊 Flooding Alert! 🌊🚨")
    print("📍 Location: [e.g. Ipswich town centre, Suffolk]")
    print("🕒 Time: [e.g. Immediate]")
    print("❗ Implications: [e.g. Potential for severe property damage and risk to life]")
    print("🏥 Health & Welfare: [e.g. Move to higher ground, avoid walking or driving through floodwaters]")
    print("📢 Advice: [e.g. Follow evacuation orders and stay tuned to local news for updates]")
    print("🛡️ Reassurance: [e.g. Emergency services are responding. Stay calm and stay safe]")
    print("🔌 Practical Implications: [e.g. Expect disruptions to traffic, power supplies, telephones, and water supplies]")
    print("📞 Helpline: [e.g. For assistance, call the Suffolk emergency helpline at 0345 606 6067]")
    print("")

elif choice == '2':
    print("\nExample of Terrorist Threat Alert:")
    print("🚨💥 Terrorist Threat Alert! 💥🚨")
    print("📍 Location: [e.g. Colchester, Essex]")
    print("🕒 Time: [e.g. 5:30 PM, February 19, 2025]")
    print("❗ Implications: [e.g. Potential for severe injury and loss of life]")
    print("🏥 Health & Welfare: [e.g. Avoid the area, stay indoors, and follow instructions from authorities]")
    print("📢 Advice: [e.g. Report any suspicious activity to the police immediately. Do not spread rumors]")
    print("🛡️ Reassurance: [e.g. Law enforcement is actively responding. Stay vigilant and stay safe]")
    print("🔌 Practical Implications: [e.g. Expect heightened security measures and possible disruptions to public transport]")
    print("📞 Helpline: [e.g. For assistance, call the Essex emergency helpline at 0345 603 7630]")
    print("")

elif choice == '3':
    print("\nExample of Public Health Emergency Alert:")
    print("🚨🦠 Public Health Emergency Alert! 🦠🚨")
    print("📍 Location: [e.g. Immediate]")
    print("🕒 Time: [e.g. Immediate]")
    print("❗ Implications: [e.g. Potential for widespread illness and health complications]")
    print("🏥 Health & Welfare: [e.g. Follow health guidelines, wear masks, and maintain social distancing]")
    print("📢 Advice: [e.g. Avoid large gatherings, wash hands frequently, and stay informed through official channels]")
    print("🛡️ Reassurance: [e.g. Health authorities are managing the situation. Stay informed and stay safe]")
    print("🔌 Practical Implications: [e.g. Expect disruptions to public services and healthcare facilities]")
    print("📞 Helpline: [e.g. For assistance, call the Essex health emergency helpline at 0300 303 9988]")
    print("")

else:
    print("Invalid choice. Exiting.")
    exit()

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
