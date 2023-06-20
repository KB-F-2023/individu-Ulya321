import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.heuristics = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = {}
        self.edges[from_node][to_node] = distance

    def add_heuristic(self, node, distance):
        self.heuristics[node] = distance

    def A_star_algorithm(self, start, goal):
        open_set = [(0, start)]
        came_from = {}
        gscore = {node: float("inf") for node in self.nodes}
        gscore[start] = 0
        fscore = {node: float("inf") for node in self.nodes}
        fscore[start] = self.heuristics[start]

        while open_set:
            current = heapq.heappop(open_set)[1]
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path
            for neighbor in self.edges[current]:
                tentative_gscore = gscore[current] + self.edges[current][neighbor]
                if tentative_gscore < gscore[neighbor]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_gscore
                    fscore[neighbor] = tentative_gscore + self.heuristics[neighbor]
                    heapq.heappush(open_set, (fscore[neighbor], neighbor))
        return None

# Generate graph
graph = Graph()

# Add nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")

# Add edges with cost
graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 3)
graph.add_edge("B", "D", 4)
graph.add_edge("B", "E", 1)
graph.add_edge("C", "F", 5)
graph.add_edge("D", "G", 3)
graph.add_edge("E", "G", 2)
graph.add_edge("F", "G", 4)

# Set heuristics
graph.add_heuristic("A", 10)
graph.add_heuristic("B", 8)
graph.add_heuristic("C", 6)
graph.add_heuristic("D", 4)
graph.add_heuristic("E", 6)
graph.add_heuristic("F", 4)
graph.add_heuristic("G", 0)

# Define start and goal
start = "A"
goal = "G"

# Run A* algorithm
path = graph.A_star_algorithm(start, goal)

# Print the result
if path:
    print(" -> ".join(path))
else:
    print("Path not found")
