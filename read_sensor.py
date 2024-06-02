"""
Module to record voltages from an ADS1115 sensor.
"""

import time
from typing import List, Generator

# pylint: disable=import-error
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
# pylint: enable=import-error


def record_voltages(max_voltage_count: int = 200,
                    num_iterations: int = 4) -> Generator[List[float], None, None]:
    """
    Records voltages from an ADS1115 sensor and yields the values.

    Args:
        max_voltage_count (int): Maximum number of values to record per iteration.
        num_iterations (int): Number of iterations to perform.

    Yields:
        list: List of measured voltages for each iteration.
    """
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        ads.gain = 2/3
        chan = AnalogIn(ads, ADS.P0)
        
        for _ in range(num_iterations):
            print("Début d'enregistrement...")
            voltages_list = []

            while len(voltages_list) < max_voltage_count:
                voltage = chan.voltage
                voltages_list.append(voltage)

            yield voltages_list
            print("Attente de 60 secondes avant la prochaine série d'enregistrements...")
            time.sleep(60)
    except (ValueError, IOError) as e:
        print("Une erreur est survenue :", e)


if __name__ == "__main__":
    for recorded_voltages in record_voltages():
        print("Tensions enregistrées :", recorded_voltages)