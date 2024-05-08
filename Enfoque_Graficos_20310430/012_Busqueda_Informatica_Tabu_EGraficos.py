import random

class TabuSearch:
    def __init__(self, initial_solution, neighbors_func, evaluate_func, tabu_tenure=5, max_iterations=100):
        self.current_solution = initial_solution
        self.tabu_list = []
        self.tabu_tenure = tabu_tenure
        self.max_iterations = max_iterations
        self.neighbors_func = neighbors_func
        self.evaluate_func = evaluate_func

    def search(self):
        iteration = 0
        best_solution = self.current_solution
        best_score = self.evaluate_func(best_solution)

        while iteration < self.max_iterations:
            neighbors = self.neighbors_func(self.current_solution)

            # Selecciona el mejor vecino que no est� en la lista tab�
            best_neighbor = min(neighbors, key=lambda x: self.evaluate_func(x) if x not in self.tabu_list else float('inf'))

            # Actualiza la lista tab�
            self.tabu_list.append(best_neighbor)
            if len(self.tabu_list) > self.tabu_tenure:
                self.tabu_list.pop(0)

            # Mueve a la mejor soluci�n vecina
            self.current_solution = best_neighbor

            # Actualiza la mejor soluci�n encontrada hasta ahora
            current_score = self.evaluate_func(self.current_solution)
            if current_score < best_score:
                best_solution = self.current_solution
                best_score = current_score

            iteration += 1

        return best_solution, best_score

# Funci�n de vecinos simple para un problema de optimizaci�n unidimensional
def simple_neighbors(solution):
    return [solution + 1, solution - 1]

# Funci�n de evaluaci�n para el mismo problema unidimensional
def simple_evaluate(solution):
    return -solution ** 2  # Minimizar la funci�n cuadr�tica

# Creamos una instancia de b�squeda tab� y ejecutamos la b�squeda
initial_solution = 0  # Estado inicial
tabu_search = TabuSearch(initial_solution, simple_neighbors, simple_evaluate)
best_solution, best_score = tabu_search.search()

# Imprimimos la mejor soluci�n encontrada
print("La mejor soluci�n encontrada es:", best_solution)
print("El mejor puntaje encontrado es:", best_score)
