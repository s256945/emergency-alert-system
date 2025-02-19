# Emergency Alert System (MQTT)

This project demonstrates a simple emergency alert system using MQTT for communication. It consists of two components:

1. **Subscriber** - Listens for emergency alerts and prints them when received.
2. **Publisher** - Sends emergency alerts to a topic that the subscriber listens to.

The communication is handled via MQTT (Message Queuing Telemetry Transport), a lightweight messaging protocol suitable for small sensors and mobile devices.

---

## Prerequisites

Before running the system, make sure you have the following:

- Python 3.x
- Mosquitto MQTT Broker (locally or remotely)

### Install Python Dependencies

You need to install the `paho-mqtt` library to handle MQTT communication. Run the following command:

```bash
pip install paho-mqtt
```

### Install Mosquitto MQTT Broker
If you don't already have an MQTT broker, you'll need to install Mosquitto locally.

## Mac
```bash
brew install mosquitto
```

**Start Mosquitto Broker**
After installation, start the Mosquitto broker with:

```bash
brew services start mosquitto
```
This will start the Mosquitto broker on the default port (1883).

## Windows
1. Download the Mosquitto installer from the official website: [Mosquitto Downloads](https://mosquitto.org/download/)
2. Run the installer and follow the installation instructions.

**Start Mosquitto Broker**
After installation, start the Mosquitto broker with:

```bash
net start mosquitto
```
This will start the Mosquitto broker on the default port (1883).

## Running the System
1. Running the Subscriber
The Subscriber listens for incoming emergency alerts on a specific MQTT topic.

Run the subscriber using:
```bash
python subscriber.py
```
The subscriber will now be listening for emergency alerts on the topic emergency/alert.

2. Running the Publisher
The Publisher sends emergency alerts to a specific MQTT topic.

While keeping the subscriber open, also run the publisher using:
```bash
python publisher.py
```
When the publisher sends an alert, the subscriber will receive and display the alert message.