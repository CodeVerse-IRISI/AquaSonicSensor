import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import numpy as np
import os

def record_voltages(max_voltage_count=200, num_iterations=4):
    """
    Enregistre les tensions mesures a partir d'un ADS1115 et renvoie les valeurs.
    
    Args:
        max_voltage_count (int): Nombre maximum de valeurs enregistrer par iteration.
        num_iterations (int): Nombre d'iterations a effectuer.
        
    Yields:
        list: Liste des tensions mesures pour chaque iteration.
    """
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        ads.gain = 2/3
        chan = AnalogIn(ads, ADS.P0)
        
        start_program_time = time.time()  # Temps de debut du programme
        
        for _ in range(4):
            print("Debut d'enregistrement...")
            voltages = []
            start_time = time.time()
            
            while len(voltages) < max_voltage_count:
                voltage = chan.voltage
                #print("Tension : {} V".format(voltage))
                voltages.append(voltage)
            
            #print("Enregistrement termine:", voltages)
            yield voltages
            
            print("Attente de 60 secondes avant la prochaine serie d'enregistrements...")
            time.sleep(60)
            
                
    except Exception as e:
        print("Une erreur est survenue :", e)
