import paho.mqtt.client as mqtt

class publisher(object):
	"""docstring for publisher"""
	def __init__(self):
		super(publisher, self).__init__()
		self.publisher = mqtt.Client()

	def run(self):
		# The callback for when the client receives a CONNACK response from the server.
		def on_connect(client, userdata, flags, rc):
		    print ("connected")
		    print("Connected with result code "+str(rc))
		    #subscribe(topic, qos=0)
		    self.publisher.subscribe("#") 
		    self.publisher.subscribe("$SYS/#") 
		    self.publisher.subscribe("EXAMPLE/output/rawData")
		    self.publisher.subscribe("EXAMPLE/input/rawData")

		 # The callback for when a PUBLISH message is received from the server.
		def on_message(client, userdata, msg):
		    print(msg.topic + " " + str(msg.payload))
		self.publisher.on_connect = on_connect
		self.publisher.on_message = on_message
		
		self.publisher.connect('127.0.0.1', 1883,60)
		print("Connection to : 127.0.0.1" )
		self.publisher.loop_forever()

def main():
	pub = publisher()
	pub.run()

if __name__=="__main__":
	main()
