import paho.mqtt.client as mqtt
import datetime




#mosquitto_sub -h mosquitto2 -t test -d
LOCAL_MQTT_HOST="mosquitto2"
LOCAL_MQTT_PORT=1883 \
LOCAL_MQTT_TOPIC="test"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
  try:
    # Returns a datetime object containing the local date and time

    # get the time object from datetime object
    ct = datetime.datetime.now().strftime("%H:%M:%S")
    print("message received!"+ct)

    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    f = open('/local_log/output'+ ct + '.jpg' ,"wb")
    f.write(msg)
    print("Image Received")
    f.close()
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()

