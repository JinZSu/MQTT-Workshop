import paho.mqtt.client as mqtt

def main():
	print("MAAAaaa GET THE CAMERA")
	#Let's make the MQTT
	#Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport ="tcp")
	client = mqtt.Client()
	print("Connection to 127.0.0.1")
	#connect_async(host, port=1883, keepalive=60, bind_address="")
	client.connect('127.0.0.1', 1883, 420)
	#publish(topic, payload=None, qos=0, retain=False)
	client.publish("floor/living","abcd", 0, False)

if __name__=="__main__":
	main()