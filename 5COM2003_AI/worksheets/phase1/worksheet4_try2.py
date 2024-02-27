# 5COM2003: Artificial Intelligence
# Worksheet 4

# Node class
class Node:
    def __init__(self, name):
        self.name = name  # Name of the node
        self.adjacentNodes = {}  # Dictionary to store adjacent nodes and their weights

    # Adds an adjacent node with a corresponding weight
    def addAdjacentNode(self, node, weight):
        self.adjacentNodes[node] = weight  

    # Returns the adjacent nodes of the current node
    def getAdjacentNodes(self):
        return self.adjacentNodes   

    # Returns the name of the node
    def getName(self):
        return self.name  

    # Displays the node and its adjacent nodes and weights
    def display(self):
        adj_nodes_string = ""
        for node, weight in self.adjacentNodes.items():
            adj_nodes_string += node + " (weight " + str(weight) + "); "
        print(self.name + " has edges to: " + adj_nodes_string)

        
# Graph class
class Graph:
    def __init__(self):
        self.nodes = {}  # Stores all nodes in the graph

    # Adds a node to the graph
    def addNode(self, node):
        self.nodes[node.name] = node

    # Adds an edge between two nodes with a weight and ensures there are no self-loops
    def addEdge(self, node1_name, node2_name, weight):
        if node1_name != node2_name:
            node1 = self.nodes[node1_name]
            node2 = self.nodes[node2_name]
            node1.addAdjacentNode(node2_name, weight)
            node2.addAdjacentNode(node1_name, weight)
        else:
            raise ValueError("Error: A node cannot be connected to itself")

    # Get all nodes in the graph
    def getNodes(self):
        return self.nodes

    # Get all edges in the graph
    def getEdges(self):
        edges = []
        visited = set()
        for node_name, node in self.nodes.items():
            for neighbour_name, weight in node.getAdjacentNodes().items():
                if (neighbour_name, node_name) not in visited:
                    edges.append((node_name, neighbour_name, weight))
                    visited.add((node_name, neighbour_name))
        return edges

    # Get the adjacent nodes for a specific node
    def getNeighbours(self, node_name):
        node = self.nodes[node_name]
        return node.getAdjacentNodes()

    # Get the weight of the edge between two nodes
    def getWeight(self, node1_name, node2_name):
        node1 = self.nodes[node1_name]
        return node1.getAdjacentNodes()[node2_name]

    # Display the graph by showing each node and its edges
    def display(self):
        for node_name, node in self.nodes.items():
            node.display()

# Create a graph
g = Graph()

# Manually create each node and add to graph
g.addNode(Node('V1'))
g.addNode(Node('V2'))
g.addNode(Node('V3'))
g.addNode(Node('V4'))
g.addNode(Node('V5'))
g.addNode(Node('V6'))

# Manually add edges between nodes
g.addEdge('V1', 'V2', 1)
g.addEdge('V1', 'V4', 3)
g.addEdge('V2', 'V3', 2)
g.addEdge('V2', 'V5', 7)
g.addEdge('V2', 'V6', 6)
g.addEdge('V3', 'V6', 4)

# Attempt to add a self-loop to see if the exception is properly raised
try:
    g.addEdge('V6', 'V6', 5)
except ValueError as e:
    print(e)

# Display the graph
g.display()
