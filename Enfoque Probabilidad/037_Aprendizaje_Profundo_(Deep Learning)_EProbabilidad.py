import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Generar datos de ejemplo (XOR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Definir el modelo de la red neuronal
modelo = Sequential()
modelo.add(Dense(4, input_dim=2, activation='relu')) # Capa oculta con 4 neuronas y funci�n de activaci�n ReLU
modelo.add(Dense(1, activation='sigmoid'))           # Capa de salida con 1 neurona y funci�n de activaci�n Sigmoide

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X, y, epochs=1000, verbose=0)

# Evaluar el modelo
puntuacion = modelo.evaluate(X, y)
print("Precisi�n del modelo:", puntuacion[1])
