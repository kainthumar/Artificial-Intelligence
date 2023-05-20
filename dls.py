class Graph_dls:


    def SetLimit(self, limit):
        self.limit = int(limit)


    def __init__(self, directed):
        self.graph = {}
        self.directed = directed
        self.limit = None

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

        if node2 in self.graph:
            self.graph[node2].append(node1)
        else:
            self.graph[node2] = [node1]

    @staticmethod
    def print_path(traced_path, goal):
        if traced_path:
            for node in traced_path:
                print(node, end=' ')


    def depth_limited_search(self, start, goals):
        visited = set()
        stack = [(start, [], 0)]

        while stack:
            current_node, traced_path, current_depth = stack.pop()

            if current_depth > limit:
                continue

            if current_node in goals:
                return traced_path + [current_node], current_node

            visited.add(current_node)

            if current_depth < limit:
                if current_node in self.graph:
                    neighbors = self.graph[current_node]
                    for neighbor in neighbors:
                        if neighbor not in visited and neighbor not in stack:
                            stack.append((neighbor, traced_path + [current_node], current_depth + 1))

        return None, None
