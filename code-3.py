from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_nodes_at_level(self, start, level):
        visited = set()
        queue = deque([(start, 0)])
        count = 0

        while queue:
            vertex, current_level = queue.popleft()

            if current_level == level:
                count += 1

            if vertex not in visited:
                visited.add(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, current_level + 1))

        return count

g = Graph()
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex: "))
target_level = int(input("Enter the target level: "))

result = g.count_nodes_at_level(start_vertex, target_level)
print(f"Number of nodes at level {target_level}: {result}")