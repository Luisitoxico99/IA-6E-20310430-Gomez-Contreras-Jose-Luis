from hmmlearn import hmm
import numpy as np

# Datos observados
observaciones = np.array([[1], [2], [3], [4], [5]])

# Definir y entrenar el modelo HMM
modelo = hmm.GaussianHMM(n_components=2, covariance_type="full", n_iter=100)
modelo.fit(observaciones)

# Filtrado
filtro_probabilidades = modelo.predict_proba(observaciones)
print("Filtrado (Probabilidades del estado actual):", filtro_probabilidades)

# Predicci�n
secuencia_futura = 2  # Longitud de la secuencia futura a predecir
prediccion_probabilidades, _ = modelo.sample(secuencia_futura)
print("Predicci�n (Probabilidades de la secuencia futura):", prediccion_probabilidades)

# Suavizado
suavizado_probabilidades = modelo.predict_proba(observaciones)
print("Suavizado (Probabilidades de los estados pasados):", suavizado_probabilidades)

# Explicaci�n
# Interpretar los resultados y explicar el comportamiento del sistema
# Por ejemplo, identificar los estados m�s probables en cada paso de tiempo
