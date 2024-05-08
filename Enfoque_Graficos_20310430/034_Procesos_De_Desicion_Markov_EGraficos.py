import numpy as np

class MarkovDecisionProcess:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor=0.9):
        self.states = states  # Lista de estados
        self.actions = actions  # Lista de acciones
        self.transition_probabilities = transition_probabilities  # Probabilidades de transici�n
        self.rewards = rewards  # Recompensas
        self.discount_factor = discount_factor  # Factor de descuento para recompensas futuras
        self.values = {state: 0 for state in states}  # Valores iniciales de los estados

    def value_iteration(self, max_iterations=100, convergence_threshold=0.01):
        # Iterar hasta que se alcance la convergencia o se llegue al n�mero m�ximo de iteraciones
        for _ in range(max_iterations):
            delta = 0  # Inicializar el cambio m�ximo de valor en esta iteraci�n
            for state in self.states:
                # Calcular el nuevo valor del estado como el m�ximo de las utilidades esperadas
                new_value = max(self.calculate_expected_utilities(state, action) for action in self.actions)
                # Calcular el cambio m�ximo de valor en esta iteraci�n
                delta = max(delta, abs(new_value - self.values[state]))
                # Actualizar el valor del estado
                self.values[state] = new_value
            # Verificar la convergencia
            if delta < convergence_threshold:
                break

    def calculate_expected_utilities(self, state, action):
        # Calcular la utilidad esperada para un par de estado-acci�n
        expected_utility = sum(prob * (self.rewards[state][action][next_state] +
                                        self.discount_factor * self.values[next_state])
                               for next_state, prob in self.transition_probabilities[state][action].items())
        return expected_utility

    def get_optimal_policy(self):
        # Obtener la pol�tica �ptima basada en los valores calculados
        policy = {}
        for state in self.states:
            # Elegir la acci�n que maximiza la utilidad esperada
            policy[state] = max(self.actions, key=lambda action: self.calculate_expected_utilities(state, action))
        return policy

# Ejemplo de uso
if __name__ == "__main__":
    # Definir estados, acciones, probabilidades de transici�n y recompensas
    states = ['Sunny', 'Rainy']
    actions = ['Stay', 'Move']
    transition_probabilities = {
        'Sunny': {
            'Stay': {'Sunny': 0.8, 'Rainy': 0.2},
            'Move': {'Sunny': 0.6, 'Rainy': 0.4}
        },
        'Rainy': {
            'Stay': {'Sunny': 0.4, 'Rainy': 0.6},
            'Move': {'Sunny': 0.2, 'Rainy': 0.8}
        }
    }
    rewards = {
        'Sunny': {'Stay': {'Sunny': 1, 'Rainy': 0}, 'Move': {'Sunny': 2, 'Rainy': 1}},
        'Rainy': {'Stay': {'Sunny': 0, 'Rainy': 1}, 'Move': {'Sunny': 1, 'Rainy': 2}}
    }

    # Crear el proceso de decisi�n de Markov
    mdp = MarkovDecisionProcess(states, actions, transition_probabilities, rewards)

    # Ejecutar la iteraci�n de valor
    mdp.value_iteration()

    # Obtener la pol�tica �ptima
    optimal_policy = mdp.get_optimal_policy()

    # Imprimir la pol�tica �ptima
    print("Pol�tica �ptima:")
    for state, action in optimal_policy.items():
        print(f"Estado: {state}, Acci�n �ptima: {action}")
