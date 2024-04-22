from kafka_producer import run_kafka_producer
from process_data import process_data
from config_reader import read_config
from predict_leak import detect_leak
import json
from read_sensor import record_voltages 

sensor_id = read_config("config.json", "sensor_id")

sensor_data = record_voltages()
# Process sensor data and print JSON string
sensor_json=process_data(sensor_id, sensor_data)

# Charger le JSON dans un dictionnaire
sensor_dict = json.loads(sensor_json)

prediction = detect_leak(sensor_dict)

if prediction :
  print("fuite detected")
  sensor_dict["leak"] = 1
  # Convertir le dictionnaire mis à jour en JSON
  updated_sensor_json = json.dumps(sensor_dict)
  
  # Envoyer les données mises à jour à Kafka
  run_kafka_producer(updated_sensor_json)
  
else:
   print("pas de fuite")

