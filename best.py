import heapq
import math

class Graph_best_first:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight
        if not self.directed:
            if v not in self.graph:
                self.graph[v] = {}
            self.graph[v][u] = weight

    def print_path(path, goal):
        for node in path:
            if node != goal:
                print(node + " -> ", end='')
            else:
                print(node)

    def set_huristics(self, H):
        self.H = H

    def heuristic(self, node, goal):
        if node in self.H:
            return self.H[node]
        if node in self.HeuristicDict:
            heuristic = self.HeuristicDict[node]
        else:
            heuristic = 0
        self.H[node] = heuristic
        return heuristic

    def best_first_search(self, start, goals):
        queue = [(0, start, [start])]
        visited = set()
        cost = {start: 0}
        while queue:
            (priority, current, path) = heapq.heappop(queue)
            if current in visited:
                continue
            visited.add(current)
            if current in goals:
                return (list(path), cost[current], current)
            if current in self.graph:
                for neighbor in self.graph[current]:
                    new_cost = cost[current] + self.graph[current][neighbor]
                    if neighbor not in visited or new_cost < cost.get(neighbor, math.inf):
                        cost[neighbor] = new_cost
                        priority =  self.heuristic(neighbor, goals[0])
                        heapq.heappush(queue, (priority, neighbor, path + [neighbor]))
        return None, None, None