import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Paso 1: Preparar los datos de entrada y salida
# Generar datos de ejemplo para la operaci�n l�gica XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
y = np.array([0, 1, 1, 0])  # Salidas correspondientes (0 para 0 XOR 0 y 1 XOR 1, y 1 para 0 XOR 1 y 1 XOR 0)

# Paso 2: Definir la arquitectura del modelo de red neuronal
modelo = Sequential()  # Crear un modelo secuencial (capas apiladas una encima de la otra)
modelo.add(Dense(4, input_dim=2, activation='relu'))  # Capa oculta con 4 neuronas y funci�n de activaci�n ReLU
modelo.add(Dense(1, activation='sigmoid'))  # Capa de salida con 1 neurona y funci�n de activaci�n Sigmoide

# Paso 3: Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Configurar el modelo para el entrenamiento, especificando la funci�n de p�rdida (entrop�a cruzada binaria), el optimizador (Adam) y las m�tricas a evaluar (precisi�n)

# Paso 4: Entrenar el modelo
modelo.fit(X, y, epochs=1000, verbose=0)  # Entrenar el modelo con los datos de entrada y salida durante 1000 �pocas

# Paso 5: Evaluar el modelo
puntuacion = modelo.evaluate(X, y)  # Evaluar el modelo con los mismos datos de entrada y salida
print("Precisi�n del modelo:", puntuacion[1])  # Imprimir la precisi�n del modelo obtenida durante la evaluaci�n
