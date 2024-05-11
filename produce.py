from confluent_kafka import Producer
import json
import time

# Test data array
test_data = [
    {
        "sensor_id": "SENSOR_001",
        "date": "2024-04-13",
        "leak": 1,
        "time": "10:35:55.499101400",
        "amplitudes": [
            0.04046630859375,
            0.04107666015625,
            # Add more data here...
        ]
    },
    # Add more data objects as needed...
]

def delivery_callback(err, msg):
    """
    Delivery callback for Kafka producer.
    """
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to topic {msg.topic()} [{msg.partition()}]')

def produce_sensor_data(producer, topic, sensor_data):
    """
    Produces sensor data to Kafka.
    """
    producer.produce(topic, key=None, value=json.dumps(sensor_data), callback=delivery_callback)

def main():
    # Kafka broker(s) address
    bootstrap_servers = '192.168.137.1:9092' 

    # Kafka topic
    topic = 'sounds'

    # Create Kafka Producer instance
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    produce_sensor_data(producer, topic, test_data[0])
    producer.flush()

if __name__ == "__main__":
    main()
