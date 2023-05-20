from collections import deque
import random
import math

class GraphSimulatedAnnealing:
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
                # print(node, end=' ')
                print("b")

    def objective_function(self, path):
        # Calculate the length of the path
        return len(path)

    def acceptance_probability(self, old_cost, new_cost, temperature):
        # Simulated annealing acceptance probability function
        if new_cost < old_cost:
            return 1.0
        return math.exp((old_cost - new_cost) / temperature)

    def simulated_annealing(self, start, goals, initial_temperature, cooling_rate):
        current_state = start
        current_path = [start]
        current_cost = self.objective_function(current_path)

        best_state = current_state
        best_path = current_path
        best_cost = current_cost

        temperature = initial_temperature

        while temperature > 0.1:
            # Generate a random neighbor
            if current_state in self.graph:
                neighbors = self.graph[current_state]
                neighbor = random.choice(neighbors)
                new_path = current_path + [neighbor]
                new_cost = self.objective_function(new_path)

                # Calculate the acceptance probability
                acceptance_prob = self.acceptance_probability(current_cost, new_cost, temperature)

                # Accept or reject the neighbor
                if acceptance_prob > random.random():
                    current_state = neighbor
                    current_path = new_path
                    current_cost = new_cost

                    # Update the best solution if necessary
                    if current_cost < best_cost:
                        best_state = current_state
                        best_path = current_path
                        best_cost = current_cost

            # Cool down the temperature
            temperature *= cooling_rate

        return best_path, best_state
