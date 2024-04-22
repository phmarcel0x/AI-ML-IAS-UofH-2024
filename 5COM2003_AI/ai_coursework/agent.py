import graph
import random
import csv

# Agent Class
class Agent:
    def __init__(self, graph):
        self.graph = graph
        self.memory = []  # Store visited nodes

    def random_walk(self, start, target):
        current_node = start
        self.memory.append(current_node)  # Store the current node in memory.
        while current_node != target:
            neighbours = current_node.get_neighbours()  # Ensure this returns Node objects.
            next_node = random.choice(neighbours)
            current_node = next_node
            self.memory.append(current_node)  # Store the new current node in memory.
        return current_node

    def shortest_path(self, start, target):
        path = self.graph.bfs_shortest_path_mod(start, target)  # Adjusted to use an existing method.
        if path:
            self.memory.extend(path[0])  # Store all nodes in the shortest path in memory.
        return path
