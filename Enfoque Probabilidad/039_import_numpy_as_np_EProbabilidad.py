from keras.models import Sequential
from keras.layers import Dense

# Crear un modelo secuencial
modelo = Sequential()

# A�adir una capa oculta con funci�n de activaci�n ReLU
modelo.add(Dense(64, input_dim=100, activation='relu'))

# A�adir una capa oculta con funci�n de activaci�n Tangente Hiperb�lica (Tanh)
modelo.add(Dense(64, activation='tanh'))

# A�adir una capa de salida con funci�n de activaci�n Sigmoide
modelo.add(Dense(10, activation='sigmoid'))

# Compilar el modelo
modelo.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
