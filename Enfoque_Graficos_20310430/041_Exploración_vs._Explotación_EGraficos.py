import numpy as np

class EpsilonGreedyPolicy:
    def __init__(self, num_actions, epsilon=0.1):
        self.num_actions = num_actions
        self.epsilon = epsilon

    def select_action(self, q_values):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.num_actions)  # Exploraci�n aleatoria
        else:
            return np.argmax(q_values)  # Explotaci�n de la mejor acci�n conocida

# Ejemplo de uso de la pol�tica epsilon-greedy
num_actions = 4
epsilon = 0.1
policy = EpsilonGreedyPolicy(num_actions, epsilon)

# Ejemplo de valores Q para cuatro acciones
q_values = np.array([0.2, 0.8, 0.5, 0.6])

# Selecci�n de acci�n utilizando la pol�tica epsilon-greedy
action = policy.select_action(q_values)
print("Acci�n seleccionada:", action)
