

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import numpy as np
import os

def record_voltages(max_voltage_count=200):
    """
    Enregistre les tensions mesurées à partir d'un ADS1115 et renvoie les valeurs.
    
    Args:
        max_voltage_count (int): Nombre maximum de valeurs à enregistrer.
        
    Yields:
        list: Liste des tensions mesurées.
    """
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        ads.gain = 2/3
        chan = AnalogIn(ads, ADS.P0)
        
        start_program_time = time.time()  # Temps de dut du programme
        
        while True:
            print("Debut d'Enregistrement...")
            voltages = []
            start_time = time.time()
            
            while True:
                voltage = chan.voltage
                print("Tension : {} V".format(voltage))
                voltages.append(voltage)
            
                # Verifier si le tableau a atteint le nombre maximum de valeurs
                if len(voltages) >= max_voltage_count:
                    break
            
            print("Enregistrement termin:", voltages)
            yield voltages
            
            print("Attente de 600 secondes avant la prochaine serie d'enregistrements...")
            time.sleep(600)
            
            # Vut du programme
            elapsed_time = time.time() - start_program_time
            if elapsed_time >= 3600:  # 3600 second 1 heure
                print("Programme termin.")
                break

    except Exception as e:
        print("Une erreur est survenue :", e)

voltages_generator = record_voltages()

for voltages in voltages_generator:
    print("Tableau de tensions enregistrer :", voltages)