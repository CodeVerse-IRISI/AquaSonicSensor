"""
Module to detect leaks based on sensor data.
"""

import time
import numpy as np  # pylint: disable=import-error
import tensorflow as tf  # pylint: disable=import-error


def detect_leak(data):
    """
    Detects a leak based on the provided sensor data.

    Args:
        data (dict): Dictionary containing sensor data with 'amplitudes' key.

    Returns:
        bool: True if a leak is detected, False otherwise.
    """
    try:
        model = tf.keras.models.load_model("model.h5")
    except FileNotFoundError:
        print("Fichier du modèle 'model.h5' non trouvé.")
        return False
    if "amplitudes" not in data:
        print("Données de capteur non fournies.")
        return False
    x = np.array(data["amplitudes"]).reshape((1, len(data["amplitudes"]), 1))
    start_time = time.time()
    leak_probability = model.predict(x)[0][0]
    end_time = time.time()
    prediction_time = end_time - start_time
    print("Temps de prédiction:", prediction_time, "secondes")
    leak_threshold = 0.5
    return leak_probability > leak_threshold
