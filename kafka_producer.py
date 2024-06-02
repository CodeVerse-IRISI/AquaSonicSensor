"""
Module to produce messages to a Kafka topic.
"""

import json
from confluent_kafka import Producer  # pylint: disable=import-error

def read_config():
    """
    Reads the client configuration from client.properties
    and returns it as a key-value map.

    Returns:
        dict: Configuration parameters.
    """
    config = {}
    with open("client.properties", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                parameter, value = line.split('=', 1)
                config[parameter] = value.strip()
    return config


def produce(topic, config, key, value):
    """
    Produces a message to the specified Kafka topic.

    Args:
        topic (str): Kafka topic name.
        config (dict): Kafka producer configuration.
        key (str): Message key.
        value (dict): Message value.
    """
    # Create a new producer instance
    producer = Producer(config)

    # Serialize the value dictionary into a JSON string and encode it into bytes
    serialized_value = json.dumps(value).encode('utf-8')

    # Produce the message
    producer.produce(topic, key=key.encode('utf-8'), value=serialized_value)
    print(f"Produced message to topic {topic}: key = {key}, value = {value}")

    # Send any outstanding or buffered messages to the Kafka broker
    producer.flush()

def run_kafka_producer(sensor_json):
    """
    Runs the Kafka producer to produce messages.

    Args:
        sensor_json (str): JSON string representing sensor data.
    """
    sensor_data = json.loads(sensor_json)
    config = read_config()
    topic = "sounds"
    key = "rasbery01"
    value = sensor_data

    produce(topic, config, key, value)
