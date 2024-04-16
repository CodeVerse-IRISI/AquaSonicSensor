from confluent_kafka import Producer
import json

def read_config():
    # reads the client configuration from client.properties
    # and returns it as a key-value map
    config = {}
    with open("client.properties") as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                config[parameter] = value.strip()
    return config

def produce(topic, config, key, value):
    # Creates a new producer instance
    producer = Producer(config)

    # Serialize the value dictionary into a JSON string and encode it into bytes
    serialized_value = json.dumps(value).encode('utf-8')

    # Produces a sample message
    producer.produce(topic, key=key.encode('utf-8'), value=serialized_value)
    print(f"Produced message to topic {topic}: key = {key} value = {value}")

    # Send any outstanding or buffered messages to the Kafka broker
    producer.flush()


def run_kafka_producer(sensor_json):
    sensor_json = json.loads(sensor_json)
    config = read_config()
    topic = "sounds"
    key = sensor_json["sensor_id"]
    value = {k: v for k, v in sensor_json.items() if k != "sensor_id"}

    produce(topic, config, key, value)