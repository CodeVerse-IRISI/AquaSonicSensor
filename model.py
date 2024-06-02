"""
Module to load data, train a DNN model, and evaluate it for leak detection.
"""

# pylint: disable=import-error
import json
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
# pylint: enable=import-error

# Charger les données depuis le fichier JSON
def load_data_from_json(file_path, max_length=None):
    """
    Charge les données à partir d'un fichier JSON.

    Args:
        file_path (str): Chemin du fichier JSON contenant les données.
        max_length (int, optional): Longueur maximale des données à charger. 
            Si spécifié, les données seront rembourrées ou tronquées à cette longueur.

    Returns:
        tuple: Un tuple contenant deux tableaux numpy, x_data et y_data.
            - x_data: Tableau numpy des données d'entrée (amplitudes).
            - y_data: Tableau numpy des étiquettes de sortie (fuite ou non).
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    x_data = []  # Liste pour stocker les données d'entrée (amplitudes)
    y_data = []  # Liste pour stocker les étiquettes de sortie (fuite ou non)
    for entry in data:
        amplitudes = entry['amplitudes']
        # Padding or trimming amplitudes to max_length
        if max_length is not None:
            if len(amplitudes) < max_length:
                amplitudes += [0.0] * (max_length - len(amplitudes))
            elif len(amplitudes) > max_length:
                amplitudes = amplitudes[:max_length]
        x_data.append(amplitudes)
        y_data.append(entry['leak'])
    return np.array(x_data), np.array(y_data)

# Spécifier le chemin du fichier JSON contenant les données
JSON_FILE_PATH = 'dataSet.json'

# Charger les données à partir du fichier JSON avec padding/truncation
# à une longueur maximale de 200 (par exemple)
x, y = load_data_from_json(JSON_FILE_PATH, max_length=200)

# Afficher les données chargées
print(x)
print(y)

# Diviser les données en ensembles d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Reshape data to fit the model input
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

# Définir le modèle DNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(
        filters=32, kernel_size=3, activation='relu', input_shape=(x_train.shape[1], 1)
    ),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Sauvegarder le modèle au format .h5
model.save("model.h5")

# Évaluer le modèle sur l'ensemble de test
loss, accuracy = model.evaluate(x_test, y_test)
print("Loss:", loss)
print("Accuracy:", accuracy)
