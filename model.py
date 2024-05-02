#pip install numpy
#pip install tensorflow
#pip install sklearn.model_selection
import json
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Charger les données depuis le fichier JSON
def load_data_from_json(file_path, max_length=None):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        
    x = []  # Liste pour stocker les données d'entrée (amplitudes)
    y = []  # Liste pour stocker les étiquettes de sortie (fuite ou non)
    for entry in data:
        amplitudes = entry['amplitudes']
        # Padding or trimming amplitudes to max_length
        if max_length is not None:
            if len(amplitudes) < max_length:
                amplitudes += [0.0] * (max_length - len(amplitudes))
            elif len(amplitudes) > max_length:
                amplitudes = amplitudes[:max_length]
        x.append(amplitudes)
        y.append(entry['leak'])
  return np.array(x), np.array(y)

# Spécifier le chemin du fichier JSON contenant les données
JSON_FILE_PATH = 'dataSet.json'

# Charger les données à partir du fichier JSON avec padding/truncation à 
# une longueur maximale de 200 (par exemple)
x, y = load_data_from_json(JSON_FILE_PATH, max_length=200)

# Afficher les données chargées
print(x)
print(y)
# Diviser les données en ensembles d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Définir le modèle CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(len(x[0]), 1)),
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
print("Loss :", loss)
print("Accuracy :", accuracy)




