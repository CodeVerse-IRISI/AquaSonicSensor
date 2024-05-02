import numpy as np
import tensorflow as tf
import time

# Fonction pour la détection de fuite
def detect_leak(data):
     """
    Detects leak based on the provided data.
    Args:
    - data (dict): Dictionary containing sensor data.
    Returns:
    - bool: True if leak is detected, False otherwise.
    """
    # Charger le modèle entraîné
    try:
        model = tf.keras.models.load_model("model.h5")
    except FileNotFoundError:
        print("Model file 'model.h5' not found.")
        return False
    except Exception as e:
        print("Error loading model:", e)
        return False

    # Check if data is provided
    if "amplitudes" not in data:
        print("Sensor data not provided.")
        return False
    
    # Charger les données du JSON
    X = np.array(data["amplitudes"]).reshape(1, len(data["amplitudes"]), 1)

    # Prédire la probabilité de fuite
    try:
         # Temps de début de la prédiction
         start_time = time.time()
         leak_probability = model.predict(X)[0][0]
         # Temps de fin de la prédiction
         end_time = time.time()
    except Exception as e:
        print("Error predicting:", e)
        return False
    # Calcul du temps écoulé
    prediction_time = end_time - start_time
    print("Temps de prédiction:", prediction_time, "secondes")

    # Seuil pour la détection de fuite 
    leak_threshold = 0.5

    # Si la probabilité de fuite est supérieure au seuil, retourner True, sinon False
    return leak_probability > leak_threshold
