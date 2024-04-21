# 5COM2003: Artificial Intelligence
# Practical Assignment: Variant A - Graph Measures
# Marcelo Hernandez: 23033126
from collections import deque
import queue

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

    # Compute DFS to retrieve goedesics from a start node
    def dfs(self, start):
        print("\nDFS from Node: ", start.get_name())

        visited = set()
        stack = [start]
        
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node.get_name())
                visited.add(node)
                stack.extend([neighbour for neighbour in node.get_neighbours() if neighbour not in visited])
        print("All nodes visited.")
    
    def display(self):
        for node in self.nodes:
            print("Node: ", node)
            # Print using list comprehension
            print("Neighbours: ", [neighbour.get_name() for neighbour in self.nodes[node].get_neighbours()])
            print()

    # Create the graph
    def create_graph(self):
        print("\nGraph Display:")
        
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
        self.nodes = graph.get_nodes()
        self.edges = graph.get_edges()
        self.node_count = graph.node_count
        self.edge_count = graph.edge_count
        
    def degree_centrality(self, node):
        return node.get_degree()  
        
    # def closeness_centrality(self):
    
    # def betweenness_centrality(self, node):
    
    def display_graph_metrics(self):
        print("Graph Centrality: ", self.graph_centrality())
        print("Closeness Centrality: ", self.closeness_centrality())
        print("Betweenness Centrality: ", self.betweenness_centrality())
    

# Create an instance of the Graph class
graph1 = Graph()
graph1.create_graph()
graph1.dfs(graph1.nodes['V5'])
