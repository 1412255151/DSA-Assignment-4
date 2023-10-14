class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def isCyclicUtil(self, v, color):
        color[v] = "gray"

        if v in self.graph:
            for neighbour in self.graph[v]:
                if color.get(neighbour, "white") == "gray":
                    return True
                elif color.get(neighbour, "white") == "white" and self.isCyclicUtil(neighbour, color):
                    return True

        color[v] = "black"
        return False

    def isCyclic(self):
        color = {node: "white" for node in self.graph}

        for node in self.graph:
            if color[node] == "white":
                if self.isCyclicUtil(node, color):
                    return True

        return False

def take_input():
    g = Graph()
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))

    for _ in range(m):
        u, v = map(int, input("Enter the edge (u, v): ").split())
        g.addEdge(u, v)

    return g

def main():
    g = take_input()
    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")

if __name__ == "__main__":
    main()