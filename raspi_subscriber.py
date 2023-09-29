    """
    This is a simple  example of subscribe to MQTT Broker
    MQTT Broker → Raspberry Pi
    """

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe Topic
    client.subscribe("raspberry/topic")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.will_set('raspberry/status', b'{"status": "Off"}')

client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()