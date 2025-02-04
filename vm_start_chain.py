#Ellen Ko
#https://github.com/ellenkko416/lab-04

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("keko/pong")
    client.message_callback_add("keko/pong", on_message_from_contchain)
    
    
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
    
def on_message_from_contchain(client, userdata, message):
   int_num = int(message.payload.decode()) +1
   print("Custom callback  - Count "+ f"{int_num}")
   client.publish("keko/ping", f"{int_num}")
   time.sleep(1)
    
    
if __name__ == '__main__':
    count = "1"
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="172.20.10.9", port=1883, keepalive=60)
    client.publish("keko/ping", count)
    client.loop_forever()
    



    	


