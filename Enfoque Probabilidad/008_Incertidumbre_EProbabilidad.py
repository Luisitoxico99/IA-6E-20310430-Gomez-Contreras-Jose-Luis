import numpy as np

# Generar datos aleatorios que representan mediciones de una variable
datos = np.random.normal(loc=10, scale=2, size=1000)  # Media=10, Desviaci�n est�ndar=2

# Calcular estad�sticas descriptivas b�sicas
media = np.mean(datos)  # Calcular la media de los datos
varianza = np.var(datos)  # Calcular la varianza de los datos
desviacion_estandar = np.std(datos)  # Calcular la desviaci�n est�ndar de los datos

# Imprimir las estad�sticas descriptivas calculadas
print("Media:", media)
print("Varianza:", varianza)
print("Desviaci�n est�ndar:", desviacion_estandar)
