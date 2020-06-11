import codecs
import json
import re
import sys

import paho.mqtt.client as mqtt
import requests

# def send_data_server(js_data): 
#     global count
#     global respond
#     #r=requests.post(url,data=js_data,headers= {'content-type':'text/json'})
#     r=requests.post(url=api_url,data=js_data,headers= {'content-type':'text/json'})
#     status=r.status_code
#     print(status) #in ra trang thai connect server
#     #print(r.text) # in ra goi data da gui toi server
#     receive=json.loads(r.text)
#     del receive['isSuccess']
#     del receive['message']
#     del receive['data']['isEnabled']
#     respond.append(receive)
#     #print(respond['data']['deviceId'])
#     # for receive in respond:
#     #     print(receive)

    
#     if r.text[13]=='1':
#         count+=1      
count=0
# MQTT_HOST = "m15.cloudmqtt.com"
# MQTT_PORT = 10111
# MQTT_KEEPALIVE_INTERVAL = 60
# MQTT_TOPIC ="HeathRate-Oxygen"
# MQTT_USER='evfdiagb'
# MQTT_PASSWORD='4MZ7kB9gHTOa'
# mqttc=mqtt.Client("nam")


MQTT_HOST = "healthcare-broker.nichietsuvn.com"
MQTT_PORT = 1883 
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC ="topic_heart_rate"
MQTT_USER='babycare'
MQTT_PASSWORD='123qaz'
mqttc=mqtt.Client("nam")
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connect success...")
    elif rc!=0:
        print("Bad connection Returned code=",rc)
    
def on_publish(client, userdata, mid):
    global count
    print("Message Published...")
    count+=1
def on_message(client, userdata, msg):
     print("Message received-> " + msg.topic + " " + str(msg.payload))
    # print('nam')
    # print(msg.topic)
    # print(msg.payload) # <- do you mean this payload = {...} ?
    # payload = json.loads(msg.payload) # you can use json.loads to convert string to json
    # print(payload['sepalWidth']) # then you can check the value
    # client.disconnect() # Got message then disconnect
def connect_server(js_data):
    global mqttc
    #mqttc=mqtt.Client(client_id="k",clean_session=True,transport="tcp")
    mqttc=mqtt.Client(client_id="nam",clean_session=True)
    mqttc=mqtt.Client()
    mqttc.on_publish = on_publish
    mqttc.on_connect = on_connect
    mqttc.on_message=on_message
    mqttc.username_pw_set(MQTT_USER,MQTT_PASSWORD)
    mqttc.connect(MQTT_HOST,MQTT_PORT,MQTT_KEEPALIVE_INTERVAL)
    mqttc.loop_start()
    #mqttc.loop_forever()
    #mqttc.publish(MQTT_TOPIC,js_data)
    #mqttc.username_pw_set(MQTT_USER,MQTT_PASSWORD)
def reconnect():
    while (mqttc.is_connected==0):
        mqttc.reconnect()
    