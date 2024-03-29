#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This example shows how you can use the MQTT client in a class.

#import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt

class MyMQTTClass(mqtt.Client):

    def __init__(self, host, port=1883, keepalive=60):
        super().__init__() # since overriding, we need to call super()
        self.host = host
        self.port = port
        self.keepalive = keepalive
        self.topics = {}
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def subscribe(self, topic, qos):
        """keep a local cache of topics subscribed to ... persist to a file if there is a crash"""
        if topic not in self.topics.keys():
            self.topics[topic] = qos
            super().subscribe(topic, qos)
        else:
            print (f"already subscribe to {topic} os of {topics[topic}")
    def run(self):
        self.connect(self.host, self.port, self.keepalive)
        self.subscribe("$SYS/#", 0)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc


if __name__ == '__main__':
    # If you want to use a specific client id, use
    # mqttc = MyMQTTClass("client-id")
    # but note that the client id must be unique on the broker. Leaving the client
    # id parameter empty will generate a random id for you.
    mqttc = MyMQTTClass("mqtt.eclipseprojects.io", 1883, 60)
    rc = mqttc.run()

    print("rc: "+str(rc))
