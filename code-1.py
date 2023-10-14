from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

g = Graph()
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex: "))
print("BFS Traversal:")
g.bfs(start_vertex)