mejor_hipotesis_actual = None
mejor_metrica = 0  # O alguna otra m�trica de evaluaci�n

for hipotesis in lista_de_hipotesis:
    metrica_actual = evaluar_hipotesis(hipotesis, datos_entrenamiento)
    if metrica_actual > mejor_metrica:
        mejor_hipotesis_actual = hipotesis
        mejor_metrica = metrica_actual

# La mejor hip�tesis encontrada hasta el momento
print("Mejor Hip�tesis Actual:", mejor_hipotesis_actual)
