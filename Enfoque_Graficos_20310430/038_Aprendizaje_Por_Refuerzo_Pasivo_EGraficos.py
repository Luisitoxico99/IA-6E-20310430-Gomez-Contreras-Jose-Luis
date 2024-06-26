import numpy as np

class PassiveReinforcementLearning:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.values = np.zeros(num_states)  # Funci�n de valor inicializada a cero

    def update(self, state, reward):
        # Actualizar la funci�n de valor utilizando la regla de actualizaci�n de Monte Carlo
        self.values[state] += self.learning_rate * (reward - self.values[state])

# Simulaci�n de un entorno de aprendizaje
class Environment:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_matrix = np.random.rand(num_states, num_actions, num_states)  # Matriz de transici�n aleatoria
        self.reward_matrix = np.random.rand(num_states, num_actions)  # Matriz de recompensa aleatoria

    def step(self, state, action):
        # Simular una transici�n de estado y una recompensa basada en la acci�n elegida
        next_state = np.random.choice(self.num_states, p=self.transition_matrix[state, action])
        reward = self.reward_matrix[state, action]
        return next_state, reward

# Simulaci�n de episodios de interacci�n y aprendizaje pasivo
def simulate_episodes(env, agent, num_episodes):
    for _ in range(num_episodes):
        state = np.random.randint(env.num_states)  # Estado inicial aleatorio
        while True:
            action = np.random.randint(env.num_actions)  # Elecci�n aleatoria de acci�n
            next_state, reward = env.step(state, action)  # Ejecutar la acci�n en el entorno
            agent.update(state, reward)  # Actualizar la funci�n de valor
            state = next_state  # Avanzar al siguiente estado

            if state == 0:  # Terminar el episodio cuando se alcanza el estado de terminaci�n
                break

# Par�metros del entorno y el agente
num_states = 5
num_actions = 2
learning_rate = 0.1
discount_factor = 0.9
num_episodes = 1000

# Crear el agente de aprendizaje por refuerzo pasivo
agent = PassiveReinforcementLearning(num_states, num_actions, learning_rate, discount_factor)

# Crear el entorno
env = Environment(num_states, num_actions)

# Simular episodios de interacci�n y aprendizaje
simulate_episodes(env, agent, num_episodes)

# Imprimir la funci�n de valor aprendida por el agente
print("Funci�n de valor aprendida por el agente:")
print(agent.values)
