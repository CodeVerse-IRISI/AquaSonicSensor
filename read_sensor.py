import time
from typing import List, Generator
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def record_voltages(max_voltage_count: int = 200, num_iterations: int = 4) -> Generator[List[float], None, None]:
    """
    Enregistre les tensions mesures à partir d'un ADS1115 et renvoie les valeurs.

    Args:
        max_voltage_count (int): Nombre maximum de valeurs à enregistrer par itération.
        num_iterations (int): Nombre d'itérations à effectuer.

    Yields:
        list: Liste des tensions mesurées pour chaque itération.
    """
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        ads.gain = 2/3
        chan = AnalogIn(ads, ADS.P0)
        start_program_time = time.time()  # Temps de début du programme
        for _ in range(num_iterations):
            print("Début d'enregistrement...")
            voltages = []
            start_time = time.time()
            while len(voltages) < max_voltage_count:
                voltage = chan.voltage
                # print("Tension : {} V".format(voltage))
                voltages.append(voltage)
                # print("Enregistrement terminé:", voltages)
            yield voltages
            print("Attente de 60 secondes avant la prochaine série d'enregistrements...")
            time.sleep(60)
    except Exception as e:
        print("Une erreur est survenue :", e)

