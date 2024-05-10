import numpy as np

# Funci�n de transici�n de estado (modelo de movimiento)
def transicion_estado(x_t_1):
    # Aqu� se define el modelo de movimiento del sistema
    # En este ejemplo, se asume un movimiento aleatorio
    return x_t_1 + np.random.normal(loc=0, scale=0.1, size=x_t_1.shape)

# Funci�n de observaci�n (modelo de medici�n)
def observacion_modelo(x_t):
    # Aqu� se define el modelo de observaci�n del sistema
    # En este ejemplo, se asume una observaci�n ruidosa
    return x_t + np.random.normal(loc=0, scale=1, size=x_t.shape)

# N�mero de part�culas
num_particulas = 1000

# Generar part�culas iniciales aleatorias
particulas = np.random.uniform(low=0, high=10, size=(num_particulas, 1))

# Iterar sobre las observaciones
for observacion in observaciones:
    # Muestrear nuevas part�culas a partir de las existentes utilizando la funci�n de transici�n de estado
    nuevas_particulas = transicion_estado(particulas)
    
    # Calcular los pesos de las part�culas basados en las observaciones
    pesos = observacion_modelo(observacion) - nuevas_particulas
    
    # Normalizar los pesos
    pesos = np.exp(-0.5 * (pesos ** 2))
    pesos /= np.sum(pesos)
    
    # Muestrear part�culas basadas en sus pesos
    indices = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos.flatten())
    particulas = nuevas_particulas[indices]
    
# Estimar el estado del sistema utilizando las part�culas finales (por ejemplo, promedio de las part�culas)
estado_estimado = np.mean(particulas)

print("Estado estimado del sistema:", estado_estimado)
 covarianza:", filtro.P)