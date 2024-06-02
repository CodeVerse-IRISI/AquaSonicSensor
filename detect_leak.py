

import numpy as np
import tensorflow as tf
import time

# Fonction pour la détection de fuite
def detect_leak(data):
    # Charger le modèle entraîné
    model = tf.keras.models.load_model("model.h5")
    # Charger les données du JSON
    X = np.array(data["amplitudes"]).reshape(1, len(data["amplitudes"]), 1)
    
    # Temps de début de la prédiction
    start_time = time.time()

    # Prédire la probabilité de fuite
    leak_probability = model.predict(X)[0][0]
    
    # Temps de fin de la prédiction
    end_time = time.time()

    # Calcul du temps écoulé
    prediction_time = end_time - start_time
    print("Temps de prédiction:", prediction_time, "secondes")

    # Seuil pour la détection de fuite 
    leak_threshold = 0.5
    
    # Si la probabilité de fuite est supérieure au seuil, retourner True, sinon False
    return leak_probability > leak_threshold


