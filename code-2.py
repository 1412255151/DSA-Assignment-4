from collections import defaultdict

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(neighbor for neighbor in reversed(graph[vertex]) if neighbor not in visited)

graph = defaultdict(list)
edges = int(input("Enter the number of edges: "))
for _ in range(edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)

start_vertex = int(input("Enter the starting vertex: "))
print("DFS Traversal:")
dfs(graph, start_vertex)