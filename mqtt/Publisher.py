from MQTTClass import MQTTClass


class Publisher(MyMQTTClass):

    def __init__(self, host, topic):
        self.mqtt =  host
        self.topic = topic

    def publish(self, topic, data):


if __name__ == '__main__':
    pub = Publisher("mqtt.eclipseprojects.io")
