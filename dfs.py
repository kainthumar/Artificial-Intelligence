class Graph_dfs:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

        if not self.directed:
            if node2 in self.graph:
                self.graph[node2].append(node1)
            else:
                self.graph[node2] = [node1]

    @staticmethod
    def print_path(traced_path, goal):
        if traced_path:
            for node in traced_path:
                print(node, end=' ')
            print(goal)

    def depth_first_search(self, start, goals):
        visited = set()
        stack = [(start, [])]

        while stack:
            current_node, traced_path = stack.pop()

            if current_node in goals:
                return traced_path, current_node

            visited.add(current_node)

            if current_node in self.graph:
                neighbors = self.graph[current_node]
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append((neighbor, traced_path + [current_node]))

        return None, None
