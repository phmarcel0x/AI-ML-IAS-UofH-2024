# 5COM2003: Artificial Intelligence
# Worksheet 4

           
# A simple node class
class Node:
    def __init__(self, name):
        self.name = name  # Name of the node
        self.adjacentNodes = {}  # Dictionary to store the adjacent nodes and their weights

    def addAdjacentNode(self, node, weight):
        self.adjacentNodes[node] = weight  # Add the adjacent node and its weight to the dictionary

    def getAdjacentNodes(self):
        return self.adjacentNodes   

    def getName(self):
        return self.name  

    def display(self):
        print(self.name + " : " + self.adjacentNodes)  # Display the node and its adjacent nodes
        
        
# A simple graph class
class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store the nodes

    def addNode(self, node):
        self.nodes[node.name] = node

    # def addEdge(self, node1_name, node2_name, weight):
    #     node1 = self.nodes[node1_name]
    #     node2 = self.nodes[node2_name]
    #     node1.addAdjacentNode(node2_name, weight)
    #     node2.addAdjacentNode(node1_name, weight)
    
    # Define a method to add an edge between two nodes with a weight making sure that no loop is created with the same node
    def addEdge(self, node1_name, node2_name, weight):
            if node1_name != node2_name:
                node1 = self.nodes[node1_name]
                node2 = self.nodes[node2_name]
                node1.addAdjacentNode(node2_name, weight)
                node2.addAdjacentNode(node1_name, weight)
            elif node1_name == node2_name:
                print("Error: A node cannot be connected to itself")

    def getNodes(self):
        return self.nodes

    def getEdges(self):
        edges = []
        for node_name, node in self.nodes.items():
            for neighbour_name, weight in node.getAdjacentNodes().items():
                edges.append((node_name, neighbour_name, weight))
        return edges

    def getNeighbours(self, node_name):
        node = self.nodes[node_name]
        return node.getAdjacentNodes()

    def getWeight(self, node1_name, node2_name):
        node1 = self.nodes[node1_name]
        return node1.getAdjacentNodes()[node2_name]

    def display(self):
        for node_name, node in self.nodes.items():
            print(node_name, ":", node.getAdjacentNodes())



# Create a graph
print()
g = Graph()
n1 = Node('V1')
n2 = Node('V2')
n3 = Node('V3')
n4 = Node('V4')
n5 = Node('V5')
n6 = Node('V6')
g.addNode(n1)
g.addNode(n2)
g.addNode(n3)
g.addNode(n4)
g.addNode(n5)
g.addNode(n6)
g.addEdge('V1', 'V2', 1)
g.addEdge('V1', 'V4', 3)
g.addEdge('V2', 'V3', 2)
g.addEdge('V2', 'V5', 7)
g.addEdge('V2', 'V6', 6)
g.addEdge('V3', 'V6', 4)
g.addEdge('V6', 'V6', 5)  # Test to see if the error message is displayed
g.display()
print()