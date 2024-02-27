# 5COM2003: Artificial Intelligence
# Worksheet 4

#######################################################
# TASK 1: Construct the graph given in the worksheet
#######################################################
# Node class
class Node:
    def __init__(self, name):
        self.name = name
        # Dictionary to store adjacent nodes, keyed by their names and valued by their weights.
        self.adjacent_nodes = {}  

    # Add an adjacent node with a corresponding weight.
    def addAdjacentNode(self, node, weight):
        self.adjacent_nodes[node] = weight  

    # Return the adjacent node(s) of the current node.
    def getAdjacentNodes(self):
        return self.adjacent_nodes   

    # Return the name of the current node.
    def getNodeName(self):
        return self.name  

    def display(self):
        adj_nodes_string = ""
        for node, weight in self.adjacent_nodes.items():
            adj_nodes_string += node + " (weight " + str(weight) + "); "
        print(self.name + " has edges to: " + adj_nodes_string)

        
# Graph class
class Graph:
    def __init__(self):
        # Dictionary to store nodes in the graph, keyed by their names.
        self.nodes = {}  

    # Add a node with a name to the graph.
    def addNode(self, node):
        self.nodes[node.name] = node

    # Add an edge between two nodes and ensure there are no self-loops (edges from a node to itself).
    def addEdge(self, node1_name, node2_name, weight):
        if node1_name != node2_name:
            node1 = self.nodes[node1_name]
            node2 = self.nodes[node2_name]
            node1.addAdjacentNode(node2_name, weight)
            node2.addAdjacentNode(node1_name, weight)
        else:
            raise ValueError("Error: Sadly, a node cannot be connected to itself.")

    # Return the node(s) in the graph.
    def getNodes(self):
        return self.nodes

    # Return the edge(s) in the graph without duplicates.
    def getEdges(self):
        edges = []  # Initialise a list to store the edges.
        visited = set()  # Initialise a set to store visited edges.
        for node_name, node in self.nodes.items():
            for neighbour_name, weight in node.getAdjacentNodes().items():
                if (neighbour_name, node_name) not in visited:
                    # If not visited, append the edge as a tuple (node, neighbor, weight).
                    edges.append((node_name, neighbour_name, weight))
                    # Add both directions of the edge to the visited set.
                    visited.add((node_name, neighbour_name))
                    visited.add((neighbour_name, node_name))
        return edges


    # Return the adjacent node(s) of a node.
    def getNodeNeighbours(self, node_name):
        node = self.nodes[node_name]
        return node.getAdjacentNodes()

    # Return the weight of an edge between two nodes.
    def getEdgeWeight(self, node1_name, node2_name):
        node1 = self.nodes[node1_name]
        return node1.getAdjacentNodes()[node2_name]

    def display(self):
        for node_name, node in self.nodes.items():
            node.display()
            

#################################################################################
# TASK 2: Implement an agent that can store the current spanning tree. 
# Give the agent the ability to sense its current node’s and edges’ information.
#################################################################################
# Agent class
class Agent:
    def __init__(self, graph, start_node):
        # Dictionary to store nodes in the spanning tree, keyed by their names. 
        self.spanning_tree_nodes = {start_node: "Node " + start_node + " is the start of the spanning tree."}
        self.spanning_tree_edges = []  # List to store edges in the spanning tree.
        self.current_node = start_node  
        self.graph = graph

    # Return the current node of the agent.
    def senseCurrentNode(self):
        return self.current_node

    # Return the edges of the current node.
    def senseEdges(self):
        return self.graph.getNodeNeighbours(self.current_node)

    # Add a node to the spanning tree.
    def addSpanningTreeNode(self, node_name):
        self.spanning_tree_nodes[node_name] = "Added node " + node_name + " to the spanning tree."

    # Add an edge to the list of spanning tree edges.
    def addSpanningTreeEdge(self, node1_name, node2_name, weight):
        self.spanning_tree_edges.append((node1_name, node2_name, weight))

    def displaySpanningTree(self):
        print("Spanning Tree Nodes: ")
        for node_name, node_description in self.spanning_tree_nodes.items():
            print(node_name + ": " + node_description)

        print("Spanning Tree Edges: ")
        for edge in self.spanning_tree_edges:
            node1, node2, weight = edge
            print("Edge from " + node1 + " to " + node2 + " with weight " + str(weight))
            
                       
# Create a graph.
print()
g = Graph()

####################################
# TASK 1 (continued):
####################################
# Create and add nodes of the graph
g.addNode(Node('V1'))
g.addNode(Node('V2'))
g.addNode(Node('V3'))
g.addNode(Node('V4'))
g.addNode(Node('V5'))
g.addNode(Node('V6'))

# Add edges between nodes
g.addEdge('V1', 'V2', 1)
g.addEdge('V1', 'V4', 3)
g.addEdge('V2', 'V3', 2)
g.addEdge('V2', 'V5', 7)
g.addEdge('V2', 'V6', 6)
g.addEdge('V3', 'V6', 4)

g.display()
print()
####################################


####################################
# TASK 2 (continued):
####################################
agent = Agent(g, 'V1')

# Display the agent's spanning tree
agent.displaySpanningTree()
print()
####################################