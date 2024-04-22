from kafka_producer import run_kafka_producer
from process_data import process_data
from config_reader import read_config
from detect_leak import detect_leak
import json


sensor_id = read_config("config.json", "sensor_id")

sensor_data = [
            -0.28692626953125,
            -0.2861328125,
            -0.28564453125,
            -0.28558349609375,
            -0.28558349609375,
            -0.285308837890625,
            -0.2850341796875,
            -0.284912109375,
            -0.28509521484375,
            -0.285369873046875,
            -0.285430908203125,
            -0.28521728515625,
            -0.284820556640625,
            -0.2847900390625,
            -0.28485107421875,
            -0.284576416015625,
            -0.283905029296875,
            -0.283111572265625,
            -0.282470703125,
            -0.281890869140625,
            -0.281219482421875,
            -0.28021240234375,
            -0.27923583984375,
            -0.2784423828125,
            -0.277496337890625,
            -0.2760009765625,
            -0.274078369140625,
            -0.27203369140625,
            -0.270294189453125,
            -0.268707275390625,
            -0.26678466796875,
            -0.26458740234375,
            -0.262664794921875,
            -0.26104736328125,
            -0.25958251953125,
            -0.258056640625,
            -0.256500244140625,
            -0.255035400390625,
            -0.253692626953125,
            -0.252716064453125,
            -0.25164794921875,
            -0.250701904296875,
            -0.2496337890625,
            -0.2490234375,
            -0.24920654296875,
            -0.2493896484375,
            -0.24945068359375,
            -0.248992919921875,
            -0.24908447265625,
            -0.24957275390625,
            -0.25030517578125,
            -0.251129150390625,
            -0.251708984375,
            -0.252471923828125,
            -0.253387451171875,
            -0.254364013671875,
            -0.255096435546875,
            -0.255523681640625,
            -0.255706787109375,
            -0.25616455078125,
            -0.25665283203125,
            -0.25726318359375,
            -0.257659912109375,
            -0.2579345703125,
            -0.258087158203125,
            -0.258392333984375,
            -0.258636474609375,
            -0.25836181640625,
            -0.25787353515625,
            -0.25732421875,
            -0.2569580078125,
            -0.25628662109375,
            -0.255157470703125,
            -0.25390625,
            -0.2529296875,
            -0.252227783203125,
            -0.251373291015625,
            -0.249755859375,
            -0.24810791015625,
            -0.2467041015625,
            -0.245574951171875,
            -0.244354248046875,
            -0.242828369140625,
            -0.2410888671875,
            -0.2396240234375,
            -0.23846435546875,
            -0.2371826171875,
            -0.23565673828125,
            -0.233612060546875,
            -0.23187255859375,
            -0.230316162109375,
            -0.229156494140625,
            -0.227935791015625,
            -0.22650146484375,
            -0.225341796875,
            -0.224639892578125,
            -0.22393798828125,
            -0.2230224609375,
            -0.221923828125,
            -0.2208251953125,
            -0.220184326171875,
            -0.219390869140625,
            -0.21868896484375,
            -0.218048095703125,
            -0.217498779296875,
            -0.217315673828125,
            -0.217193603515625,
            -0.216949462890625,
            -0.21673583984375,
            -0.216766357421875,
            -0.216827392578125,
            -0.21673583984375,
            -0.216461181640625,
            -0.216064453125,
            -0.215850830078125,
            -0.21588134765625,
            -0.215850830078125,
            -0.215789794921875,
            -0.21539306640625,
            -0.21502685546875,
            -0.2147216796875,
            -0.21453857421875,
            -0.214569091796875,
            -0.214263916015625,
            -0.2137451171875,
            -0.213134765625,
            -0.212005615234375,
            -0.210784912109375,
            -0.209320068359375,
            -0.20758056640625,
            -0.205780029296875,
            -0.203887939453125,
            -0.202362060546875,
            -0.200927734375,
            -0.199615478515625,
            -0.197845458984375,
            -0.19580078125,
            -0.193328857421875,
            -0.190185546875,
            -0.186614990234375,
            -0.18280029296875,
            -0.1790771484375,
            -0.17535400390625,
            -0.172027587890625,
            -0.168731689453125,
            -0.165435791015625,
            -0.16217041015625,
            -0.158477783203125,
            -0.15447998046875,
            -0.15032958984375,
            -0.145904541015625,
            -0.141448974609375,
            -0.137359619140625,
            -0.133544921875,
            -0.12994384765625,
            -0.126312255859375,
            -0.122802734375,
            -0.11932373046875,
            -0.115814208984375,
            -0.11248779296875,
            -0.1090087890625,
            -0.105438232421875,
            -0.102142333984375,
            -0.099151611328125,
            -0.096527099609375,
            -0.093902587890625,
            -0.091156005859375,
            -0.088226318359375,
            -0.08544921875,
            -0.082550048828125,
            -0.0797119140625,
            -0.076934814453125,
            -0.074310302734375,
            -0.07208251953125,
            -0.069793701171875,
            -0.06732177734375,
            -0.064361572265625,
            -0.061309814453125,
            -0.05828857421875,
            -0.054962158203125,
            -0.05133056640625,
            -0.047393798828125,
            -0.043731689453125,
            -0.0404052734375,
            -0.03753662109375,
            -0.034393310546875,
            -0.030853271484375,
            -0.027069091796875,
            -0.0230712890625,
            -0.01861572265625,
            -0.0135498046875,
            -0.0084228515625,
            -0.003662109375,
            0.000335693359375,
            0.004150390625,
            0.008087158203125,
            0.0120849609375,
            0.016448974609375,
            0.0208740234375,
            0.025390625
        ]
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

