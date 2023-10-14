from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def count_trees(self):
        visited = set()
        count = 0
        for vertex in self.graph:
            if vertex not in visited:
                count += 1
                self.dfs(vertex, visited)
        return count

g = Graph()
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

result = g.count_trees()
print(f"Number of trees in the forest: {result}")