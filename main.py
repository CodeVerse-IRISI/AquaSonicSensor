from kafka_producer import run_kafka_producer
from process_data import process_data
from config_reader import read_config
from detect_leak import detect_leak
import json
from read_sensor import record_voltages

sensor_id = read_config("config.json", "sensor_id")

voltages_generator = record_voltages(max_voltage_count=200)


for voltages in voltages_generator:
    print("Tableau de tensions enregistrer :", voltages)
     
    sensor_data= voltages

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

    time.sleep(300)  # Attendre 5 minutes entre chaque iteration
