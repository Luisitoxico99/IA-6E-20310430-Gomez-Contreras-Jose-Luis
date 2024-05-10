import tensorflow as tf

# Definir el modelo de red neuronal recurrente (RNN)
modelo_rnn = tf.keras.Sequential([
    tf.keras.layers.LSTM(128, input_shape=(None, 13)),  # Capa LSTM con 128 unidades
    tf.keras.layers.Dense(64, activation='relu'),      # Capa densa con 64 neuronas y funci�n de activaci�n ReLU
    tf.keras.layers.Dense(10, activation='softmax')    # Capa de salida con 10 neuronas y funci�n de activaci�n Softmax
])

# Compilar el modelo
modelo_rnn.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

# Entrenar el modelo con datos de entrenamiento
modelo_rnn.fit(datos_entrenamiento, etiquetas_entrenamiento, epochs=10, batch_size=32)

# Evaluar el modelo con datos de prueba
puntuacion = modelo_rnn.evaluate(datos_prueba, etiquetas_prueba)
print("Precisi�n del modelo:", puntuacion[1])
