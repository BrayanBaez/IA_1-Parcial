import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("Distancia mínima desde el origen:")
        for node in range(self.V):
            print("Nodo", node, "-> Distancia:", dist[node])

    def min_distance(self, dist, visited):
        min_value = sys.maxsize

        for v in range(self.V):
            if dist[v] < min_value and not visited[v]:
                min_value = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not visited[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


# Ejemplo de uso
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

g.dijkstra(0)
