# Definici�n de la clase para representar una red de decisi�n
class DecisionNetwork:
    def __init__(self):
        self.nodes = {}  # Diccionario para almacenar los nodos de la red de decisi�n y sus probabilidades

    def add_node(self, node_name, probabilities):
        self.nodes[node_name] = probabilities  # Agregar nodo con sus probabilidades

    def value_of_information(self, uncertain_variable):
        # Calcular la utilidad esperada antes de conocer la informaci�n
        initial_expected_utility = self.expected_utility()

        # Calcular la utilidad esperada despu�s de conocer la informaci�n
        updated_expected_utility = 0
        for value, probability in self.nodes[uncertain_variable].items():
            # Actualizar la probabilidad del nodo de la variable incierta
            self.nodes[uncertain_variable] = {value: probability}
            # Calcular la nueva utilidad esperada
            updated_expected_utility += probability * self.expected_utility()

        # Calcular el valor de la informaci�n como la diferencia en la utilidad esperada
        value_of_information = updated_expected_utility - initial_expected_utility
        return value_of_information

    def expected_utility(self):
        # Simplemente como ejemplo, asumimos que la utilidad esperada es la suma de las utilidades ponderadas por las probabilidades
        expected_utility = sum(prob * utility for prob, utility in self.calculate_outcome_probabilities())
        return expected_utility

    def calculate_outcome_probabilities(self):
        # Calcular las probabilidades de los resultados posibles
        outcome_probabilities = []
        for values in zip(*self.nodes.values()):
            probability = 1
            for prob in values:
                probability *= prob
            outcome_probabilities.append(probability)
        return outcome_probabilities

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una red de decisi�n con nodos y probabilidades
    network = DecisionNetwork()
    network.add_node('Lluvia', {'S�': 0.2, 'No': 0.8})
    network.add_node('Tr�fico', {'S�': 0.6, 'No': 0.4})
    network.add_node('Llegar_Tarde', {
        ('S�', 'S�'): 0.9, ('S�', 'No'): 0.6,
        ('No', 'S�'): 0.7, ('No', 'No'): 0.3
    })

    # Calcular el valor de la informaci�n de la variable 'Lluvia'
    voi = network.value_of_information('Lluvia')

    # Imprimir el valor de la informaci�n
    print("El valor de la informaci�n de la variable 'Lluvia' es:", voi)
