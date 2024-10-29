# Tarea:
    # Desarrolla una clase que represente un grafo dirigido, utilizando una matriz de adyacencia.
    # La clase debe incluir los siguientes métodos:
    # Agregar nodos: Añadir nuevos nodos al grafo.
    # Agregar aristas: Definir las conexiones entre los nodos en la matriz de adyacencia.
    # Mostrar la matriz de adyacencia: Visualizar la matriz que representa el grafo.

class GrafoDirigido:
    def __init__(self, num_nodos):
        self.num_nodos = num_nodos
        self.matriz_adyacencia = [[0 for _ in range(num_nodos)] for _ in range(num_nodos)]

    def agregar_arista(self, origen, destino):
        if 0 <= origen < self.num_nodos and 0 <= destino < self.num_nodos:
            self.matriz_adyacencia[origen][destino] = 1
        else:
            print("Nodo inválido")

    def mostrar_matriz_adyacencia(self):
        for fila in self.matriz_adyacencia:
            print(fila)

# Ejemplo de uso grafo
grafo = GrafoDirigido(5)  # Crea un grafo con 5 nodos

# Agregar aristas
grafo.agregar_arista(0, 1)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 0)

# Mostrar la matriz de adyacencia
grafo.mostrar_matriz_adyacencia()