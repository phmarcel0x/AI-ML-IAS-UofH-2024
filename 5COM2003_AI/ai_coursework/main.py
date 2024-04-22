# 5COM2003: Artificial Intelligence
# Practical Assignment: Variant A - Graph Measures
# Marcelo Hernandez: 23033126
# main.py

import graph as g
import agent as a
import random
import csv

# Create an instance of the Graph class
g1 = g.Graph()  
g1.create_graph()
a1 = a.Agent(g1)

# print("\nBFS SHORTEST PATH RESULTS:")
# for node in g1.nodes:
#     g1.display_bfs(g1.nodes[node])

# metrics_g1 = g.GraphMetrics(g1)
# metrics_g1.display()

# Run simulations
simulations = 1000
results = []

for _ in range(simulations):
    nodes_list = list(g1.get_nodes().values())  # Convert node objects to a list
    start = random.choice(nodes_list)  # Randomly choose a start node
    target = random.choice(nodes_list)  # Randomly choose a target node
    while target == start:
        target = random.choice(nodes_list)  # Ensure start and target are not the same

    # Random Walk simulation
    a1.memory = []
    a1.random_walk(start, target)  # Ensure this method accepts Node objects
    random_walk_nodes_visited = len(a1.memory)

    # Shortest Path simulation
    a1.memory = []
    a1.shortest_path(start, target)  # Ensure this method accepts Node objects
    shortest_path_nodes_visited = len(a1.memory)

    results.append([start.get_name(), target.get_name(), random_walk_nodes_visited, shortest_path_nodes_visited])

# Save results to a CSV file inside the ai_coursework folder
filename = "ai_cw_results.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Start Node", "Target Node", "Random Walk Nodes Visited", "Shortest Path Nodes Visited"])
    writer.writerows(results)

print("Simulations completed and results saved to", filename)