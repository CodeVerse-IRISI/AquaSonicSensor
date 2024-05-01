import time
import json
from kafka_producer import run_kafka_producer
from process_data import process_data
from config_reader import read_config
from detect_leak import detect_leak
from read_sensor import record_voltages

def main():
    """
    Main function to run the sensor data processing and leak detection.
    """
    # Read sensor ID from config
    sensor_id = read_config("config.json", "sensor_id")

    # Generator for reading voltages
    voltages_generator = record_voltages(max_voltage_count=200)

    for voltages in voltages_generator:
        print("Voltages recorded:", voltages)

        # Process sensor data
        sensor_json = process_data(sensor_id, voltages)

        # Load JSON into dictionary
        sensor_dict = json.loads(sensor_json)

        # Detect leak
        prediction = detect_leak(sensor_dict)

        if prediction:
            print("Leak detected")
            sensor_dict["leak"] = 1
        else:
            print("No leak")

        # Convert updated dictionary back to JSON
        updated_sensor_json = json.dumps(sensor_dict)

        # Send updated data to Kafka
        run_kafka_producer(updated_sensor_json)

        time.sleep(300)  # Wait for 5 minutes between each iteration

if __name__ == "__main__":
    main()
