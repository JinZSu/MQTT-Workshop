import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # if(rc==0):
    # 	print ("connected")
    # else:
    # 	client.subscribe("digging/#")
    client.subscribe("office/light")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client("HELLO")
client.on_connect = on_connect
client.on_message = on_message
print("PreConnect")
client.connect("127.0.0.1", 1883, 60)
print("CONNECTED")
client.publish("office/light","abcd", 0, False)
client.loop_forever()

#mosquitto_pub -t office/light -m "CLAP ON CLAP OFF THE CLAPPER"
#mosquitto_sub -t office/light