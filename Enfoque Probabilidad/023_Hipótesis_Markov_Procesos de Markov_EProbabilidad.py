import numpy as np

# Definimos los estados posibles
estados = ['lluvioso', 'soleado']

# Definimos la matriz de transici�n de probabilidad
# En este ejemplo, usamos una matriz de transici�n de primer orden
# Donde las filas representan el estado actual y las columnas representan el pr�ximo estado
matriz_transicion = np.array([
    [0.7, 0.3],  # Probabilidad de transici�n de lluvioso a lluvioso y soleado
    [0.4, 0.6]   # Probabilidad de transici�n de soleado a lluvioso y soleado
])

# Definimos el estado inicial
estado_actual = np.random.choice(estados)

# Definimos la longitud de la secuencia que queremos generar
longitud_secuencia = 10

# Generamos una secuencia de estados utilizando el proceso de Markov
secuencia_estados = [estado_actual]
for _ in range(longitud_secuencia - 1):
    estado_siguiente = np.random.choice(estados, p=matriz_transicion[estados.index(estado_actual)])
    secuencia_estados.append(estado_siguiente)
    estado_actual = estado_siguiente

# Imprimimos la secuencia de estados generada
print("Secuencia de estados generada:", secuencia_estados)
