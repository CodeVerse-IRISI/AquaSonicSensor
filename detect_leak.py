pip install numpy
pip install tensorflow

import time
import numpy as np
import tensorflow as tf
  
def detect_leak(data):
    """
    Detects leak based on the provided data.
    Args:
    - data (dict): Dictionary containing sensor data.
    Returns:
    - bool: True if leak is detected, False otherwise.
    """
    # Load the trained model
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
    
    # Reshape data for prediction
    x = np.array(data["amplitudes"]).reshape(1, len(data["amplitudes"]), 1)
    
    # Predict leak probability
    try:
        start_time = time.time()
        leak_probability = model.predict(x)[0][0]
        end_time = time.time()
    except Exception as e:
        print("Error predicting:", e)
        return False
    
    # Calculate prediction time
    prediction_time = end_time - start_time
    print("Prediction time:", prediction_time, "seconds")

    # Threshold for leak detection
    leak_threshold = 0.5
    
    # Return True if leak probability is above threshold, False otherwise
    return leak_probability > leak_threshold
