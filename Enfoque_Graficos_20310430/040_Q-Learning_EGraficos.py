import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_values = np.zeros((num_states, num_actions))  # Funci�n de valor Q inicializada a cero

    def choose_action(self, state):
        # Selecci�n de una acci�n utilizando la pol�tica epsilon-greedy
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.num_actions)  # Exploraci�n aleatoria
        else:
            return np.argmax(self.q_values[state])  # Explotaci�n de la mejor acci�n conocida

    def update(self, state, action, reward, next_state):
        # Actualizaci�n de la funci�n de valor Q utilizando la regla de actualizaci�n de Q-learning
        target = reward + self.discount_factor * np.max(self.q_values[next_state])
        self.q_values[state, action] += self.learning_rate * (target - self.q_values[state, action])

# Simulaci�n de un entorno de aprendizaje
class Environment:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_matrix = np.random.rand(num_states, num_actions, num_states)  # Matriz de transici�n aleatoria
        self.reward_matrix = np.random.rand(num_states, num_actions)  # Matriz de recompensa aleatoria

    def step(self, state, action):
        # Simulaci�n de una transici�n de estado y una recompensa basada en la acci�n elegida
        next_state = np.random.choice(self.num_states, p=self.transition_matrix[state, action])
        reward = self.reward_matrix[state, action]
        return next_state, reward

# Simulaci�n de episodios de interacci�n y aprendizaje con Q-Learning
def simulate_episodes(env, agent, num_episodes):
    for _ in range(num_episodes):
        state = np.random.randint(env.num_states)  # Estado inicial aleatorio
        while True:
            action = agent.choose_action(state)  # Selecci�n de acci�n basada en la pol�tica
            next_state, reward = env.step(state, action)  # Ejecutar la acci�n en el entorno
            agent.update(state, action, reward, next_state)  # Actualizar la funci�n de valor Q
            state = next_state  # Avanzar al siguiente estado

            if state == 0:  # Terminar el episodio cuando se alcanza el estado de terminaci�n
                break

# Par�metros del entorno y el agente
num_states = 5
num_actions = 2
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1
num_episodes = 1000

# Crear el agente de Q-Learning
agent = QLearning(num_states, num_actions, learning_rate, discount_factor, epsilon)

# Crear el entorno
env = Environment(num_states, num_actions)

# Simular episodios de interacci�n y aprendizaje con Q-Learning
simulate_episodes(env, agent, num_episodes)

# Imprimir la funci�n de valor Q aprendida por el agente
print("Funci�n de valor Q aprendida por el agente:")
print(agent.q_values)
