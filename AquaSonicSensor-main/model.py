#!pip install tensorflow

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Charger les données depuis le fichier JSON
def load_data_from_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    X = []  # Liste pour stocker les données d'entrée (amplitudes)
    y = []  # Liste pour stocker les étiquettes de sortie (fuite ou non)

    for entry in data:
        X.append(entry['amplitudes'])
        y.append(entry['leak'])

    return np.array(X), np.array(y)


# Spécifier le chemin du fichier JSON contenant les données
json_file_path = 'C:\\Users\\pc\\Desktop\\documents_conduit\\sensor_data.json'

# Charger les données à partir du fichier JSON
X, y = load_data_from_json(json_file_path)

# Afficher les données chargées
print(X)
print(y)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Définir le modèle CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(len(X[0]), 1)),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compiler le modèle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Évaluer le modèle sur l'ensemble de test
loss, accuracy = model.evaluate(X_test, y_test)
print("Loss :", loss)
print("Accuracy :", accuracy)
