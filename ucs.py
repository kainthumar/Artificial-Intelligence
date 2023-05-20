from queue import PriorityQueue


class Graph_ucs:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))
        if not self.directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append((u, cost))

    def uniform_cost_search(self, start, goals):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, start, [start]))  # (cost, vertex, path)

        while not queue.empty():
            cost, vertex, path = queue.get()

            if vertex not in visited:
                if vertex in goals:
                    return path, vertex

                visited.add(vertex)

                for neighbor, edge_cost in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        new_cost = int(cost) + int(edge_cost)
                        queue.put((new_cost, neighbor, path + [neighbor]))

        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path), end=' ')
        print('-> Goal: %s' % goal)
