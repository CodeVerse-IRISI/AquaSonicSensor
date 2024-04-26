import json
from datetime import datetime
from config_reader import read_config

def process_data(sensor_id, sensor_data):
    """
    Process sensor data and form a JSON structure.

    Args:
        sensor_id (str): Identifier for the sensor.
        sensor_data (list): List of sensor data readings.

    Returns:
        str: JSON string representing the processed data.
    """
    # Form JSON structure
    processed_data = {
        "sensor_id": sensor_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amplitudes": sensor_data,
        "leak": None,  # Placeholder for leak detection status
        "time": datetime.now().strftime("%H:%M:%S.%f")
    }

    # Convert dictionary to JSON string
    json_string = json.dumps(processed_data, indent=4)

    return json_string
