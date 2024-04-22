# 5COM2003: Artificial Intelligence
# Practical Assignment: Variant A - Graph Measures
# Marcelo Hernandez: 23033126
# graph.py

from collections import deque
import networkx as nx

# Node Class
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
    
    def get_neighbours(self):
        return self.neighbours
    
    def get_name(self):
        return self.name

    def get_degree(self):
        return len(self.neighbours)


# Edge Class
class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
    
    def get_nodes(self):
        return self.node1, self.node2


# Undirected Graph Class
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.node_count = 0  # Initialise the node count
        self.edge_count = 0  # Initialise the edge count
        
    def add_node(self, node):
        self.nodes[node.get_name()] = node
        self.node_count += 1
        
    def add_edge(self, edge):
        node1, node2 = edge.get_nodes()
        self.nodes[node1.get_name()].add_neighbour(node2)
        self.nodes[node2.get_name()].add_neighbour(node1)
        self.edges.append(edge)
        self.edge_count += 1
        
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.edges

    def bfs_shortest_path(self, start):
        distances = {}
        queue = deque([start])  # Start with the start node
        distances[start.get_name()] = 0  # Distance to itself is 0

        while queue:
            node = queue.popleft()
            current_distance = distances[node.get_name()]            
            for neighbour in node.get_neighbours():
                if neighbour.get_name() not in distances:  # Check if not visited
                    queue.append(neighbour)
                    distances[neighbour.get_name()] = current_distance + 1                  
        return distances
    
    def bfs_shortest_path_mod(self, start, target):
        queue = deque([(start, [start.get_name()])])  # Only the start node (start) is in the path
        visited = set()
        shortest_paths = []  # List to store the shortest paths
        shortest_length = float('inf')  # Infinity to compare with the length of the paths

        while queue:
            current_node, path = queue.popleft()
            if current_node not in visited or len(path) <= shortest_length:
                visited.add(current_node)
                # If the current node is the end node (target), add the path to the shortest_paths
                if current_node == target:
                    shortest_length = len(path)
                    shortest_paths.append(path)
                # Extend the path to the neighbors not yet visited
                for neighbor in current_node.get_neighbours():
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor.get_name()]))

        # Return only the shortest paths from the collected paths
        return [p for p in shortest_paths if len(p) == shortest_length]
    
    def display_bfs(self, start):
        distances = self.bfs_shortest_path(start)
        print(f"{start.get_name()} to: {distances} => SUM = {sum(distances.values())}")
    
    def display(self):
        for node in self.nodes:
            # Print using list comprehension
            print(f"{node} neighbours: {[neighbour.get_name() for neighbour in self.nodes[node].get_neighbours()]}")

    # Create the graph
    def create_graph(self):
        print("\nGRAPH DISPLAY:")
        
        for i in range(1, 8):
            self.add_node(Node('V' + str(i)))
        
        self.add_edge(Edge(self.nodes['V1'], self.nodes['V2']))
        self.add_edge(Edge(self.nodes['V2'], self.nodes['V3']))
        self.add_edge(Edge(self.nodes['V3'], self.nodes['V4']))
        self.add_edge(Edge(self.nodes['V4'], self.nodes['V5']))
        self.add_edge(Edge(self.nodes['V3'], self.nodes['V6']))
        self.add_edge(Edge(self.nodes['V6'], self.nodes['V7']))
        self.add_edge(Edge(self.nodes['V7'], self.nodes['V4']))

        self.display()
    
            
# Graph Metrics Class
# As defined in Clements (2019)
class GraphMetrics:
    def __init__(self, graph):        
        self.graph = graph
        
    def degree_centrality(self, node):
        # return node.get_degree()
        print(f"- {node.get_name()} Degree Centrality = {node.get_degree()}")  
       
    def closeness_centrality(self, node):
        distances = self.graph.bfs_shortest_path(node)
        total_distance = sum(distances.values())
        closeness_cent = 0
        if total_distance > 0:
            closeness_cent = 1 / total_distance
            print(f"- {node.get_name()} Closeness Centrality = {closeness_cent:.5f}")
        return closeness_cent
    
    def betweenness_centrality(self, node):
        betweenness = 0
        nodes = self.graph.get_nodes().values()
        for start in nodes:
            for target in nodes:
                if start != target and start != node and target != node:
                    all_paths = self.graph.bfs_shortest_path_mod(start, target)
                    shortest_paths_through_v = [path for path in all_paths if node.get_name() in path]
                    betweenness += len(shortest_paths_through_v) / len(all_paths) if all_paths else 0
        print(f"- {node.get_name()} Betweenness Centrality = {betweenness}")
        return betweenness
    
    # Display the metrics for all nodes
    def display(self):
        print("\nGRAPH METRICS:")
        for node in self.graph.get_nodes().values():
            self.degree_centrality(node)
            self.closeness_centrality(node)
            self.betweenness_centrality(node)
            print()
            
    # # Compare results with NetworkX
    # def compare(self):
    #     print("\nNETWORKX METRICS:")
    #     G = nx.Graph()
    #     for edge in self.graph.get_edges():
    #         node1, node2 = edge.get_nodes()
    #         G.add_edge(node1.get_name(), node2.get_name())
        
    #     nx_metrics = nx.closeness_centrality(G)
    #     for node in self.graph.get_nodes().values():
    #         print(f"- {node.get_name()} Closeness Centrality = {nx_metrics[node.get_name()]:.5f}")
            
    #     nx_metrics = nx.betweenness_centrality(G, normalized=False)
    #     for node in self.graph.get_nodes().values():
    #         print(f"- {node.get_name()} Betweenness Centrality = {nx_metrics[node.get_name()]}")
            
    #     nx_metrics = nx.degree_centrality(G)
    #     for node in self.graph.get_nodes().values():
    #         print(f"- {node.get_name()} Degree Centrality = {nx_metrics[node.get_name()]}")
            
    #     print()