# Definimos la funci�n para la b�squeda bidireccional
def bidirectional_search(graph, start, goal):
    # Inicializamos dos conjuntos de nodos visitados, uno para cada direcci�n de b�squeda
    visited_forward = {start}
    visited_backward = {goal}
    
    # Inicializamos dos colas, una para cada direcci�n de b�squeda
    queue_forward = [start]
    queue_backward = [goal]
    
    # Mientras ambas colas no est�n vac�as
    while queue_forward and queue_backward:
        # Realizamos la b�squeda hacia adelante desde la cola forward
        node_forward = queue_forward.pop(0)
        
        # Imprimimos el nodo que estamos visitando en la b�squeda hacia adelante
        print("Visitando nodo hacia adelante:", node_forward)
        
        # Si encontramos una intersecci�n entre las b�squedas hacia adelante y hacia atr�s, hemos terminado
        if node_forward in visited_backward:
            print("�Intersecci�n encontrada en el nodo:", node_forward, "!")
            return True
        
        # Expandimos los nodos vecinos del nodo actual en la b�squeda hacia adelante
        for neighbor in graph[node_forward]:
            if neighbor not in visited_forward:
                visited_forward.add(neighbor)
                queue_forward.append(neighbor)
        
        # Realizamos la b�squeda hacia atr�s desde la cola backward
        node_backward = queue_backward.pop(0)
        
        # Imprimimos el nodo que estamos visitando en la b�squeda hacia atr�s
        print("Visitando nodo hacia atr�s:", node_backward)
        
        # Si encontramos una intersecci�n entre las b�squedas hacia adelante y hacia atr�s, hemos terminado
        if node_backward in visited_forward:
            print("�Intersecci�n encontrada en el nodo:", node_backward, "!")
            return True
        
        # Expandimos los nodos vecinos del nodo actual en la b�squeda hacia atr�s
        for neighbor in graph[node_backward]:
            if neighbor not in visited_backward:
                visited_backward.add(neighbor)
                queue_backward.append(neighbor)
    
    # Si no encontramos una intersecci�n, la b�squeda no tuvo �xito
    print("No se encontr� intersecci�n.")
    return False

# Grafo de ejemplo representado como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Nodo de inicio y nodo objetivo para la b�squeda bidireccional
start_node = 'A'
goal_node = 'F'

# Llamamos a la funci�n de b�squeda bidireccional con el grafo, el nodo de inicio y el nodo objetivo
result = bidirectional_search(graph, start_node, goal_node)

# Imprimimos el resultado de la b�squeda
if result:
    print("�Se encontr� un camino entre", start_node, "y", goal_node, "!")
else:
    print("No se encontr� un camino entre", start_node, "y", goal_node, ".")

