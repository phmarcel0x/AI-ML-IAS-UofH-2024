# 5COM2003: Artificial Intelligence
# Worksheet 4

###################################################################################################
# TASK 1: Construct the graph given in the worksheet.
###################################################################################################
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
        print(self.name + " has edge(s) to: " + adj_nodes_string)


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
        print("Initial, beautiful graph...")
        for node in self.nodes.values():
            node.display()


###################################################################################################
# TASK 2: Implement an agent that can store the current spanning tree. 
# Give the agent the ability to sense its current node’s and edges’ information.
###################################################################################################
# Agent class
class Agent:
    def __init__(self, graph, start_node):
        # Dictionary to store nodes in the spanning tree, keyed by their names. 
        self.spanning_tree_nodes = {start_node: "Set node " + start_node + " as the start of the spanning tree."}
        self.spanning_tree_edges = []  # List to store edges in the spanning tree.
        self.current_node = start_node  
        self.graph = graph
        self.memory = {}  # TASK 4: Add spanning tree candidates to the agent's memory.
        self.visited = set()  # TASK 5: Add a set to store visited nodes.

    # Return the current node of the agent.
    def senseCurrentNode(self):
        return self.current_node

    # Return the edges of the current node.
    def senseEdges(self):
        return self.graph.getNodeNeighbours(self.current_node)
    
    def storeSpanningTree(self, node_name, added_node_msg, edge):
        self.spanning_tree_nodes[node_name] = added_node_msg  # New node message includes the node name.
        self.spanning_tree_edges.append(edge)  
        
    def exposeSensoryInformation(self):
        print("Agent's spidey senses are tingling...")
        print("Senses it is at node: " + self.senseCurrentNode() + ".")
        neighbours = self.senseEdges()  
        adj_nodes_string = ""  
        for node, weight in neighbours.items():  
            adj_nodes_string += node + " (weight " + str(weight) + "); " 
        print("Senses neighbouring edges to: " + adj_nodes_string)

    def exposeSpanningTree(self):
        print("\nAgent's totally legitimate spanning tree - in order of expansion...")
        for edge in self.spanning_tree_edges:
            node1, node2, weight = edge
            print("Edge from " + node1 + " to " + node2 + " with weight " + str(weight))
             
    ###################################################################################################
    # Task 3: Function to chose the next edge to add to the spanning tree based on the minimum weight.
    ###################################################################################################
    def choseNextEdgePrimAlgo(self):
        permitted_edges = {}
        for node in self.spanning_tree_nodes:
            for adj_node, weight in self.graph.getNodeNeighbours(node).items():
                if adj_node not in self.spanning_tree_nodes:
                    permitted_edges[(node, adj_node)] = weight
        
        # Spanning tree is complete if there are no permitted edges.
        if not permitted_edges:
            return None
        
        # Find minimally weighted edge.
        min_edge = min(permitted_edges, key=permitted_edges.get)
        min_weight = permitted_edges[min_edge]
        
        # Add the new edge to the spanning tree.
        node1, new_node = min_edge  # Unpack the new node from the edge tuple.
        edge_with_weight = min_edge + (min_weight,)  # Add the new weight (one-element-tuple,) to the edge tuple.
        self.storeSpanningTree(new_node, "Added node " + new_node + " to the spanning tree.", edge_with_weight)
        self.current_node = new_node
        
        return min_edge
    
    ###################################################################################################
    # TASK 4: Add memoery to the agent. 
    # Pretty much the same as choseNextEdgePrimAlgo(), but with memory instead of local variables.
    ###################################################################################################
    def updateMemory(self):
        self.memory.clear()
        for node in self.spanning_tree_nodes:
            for adj_node, weight in self.graph.getNodeNeighbours(node).items():
                if adj_node not in self.spanning_tree_nodes:
                    self.memory[(node, adj_node)] = weight
             
    # Return the candidate edges for the next edge to add to the spanning tree.       
    def getCandidatesFromMemory(self):
        return self.memory
    
    def choseNextEdgePrimAlgoWithMemory(self):
        self.updateMemory()
        
        # Spanning tree is complete if there are no permitted edges.
        if not self.memory:
            return None
    
        # Find minimally weighted edge.
        min_edge = min(self.memory, key=self.memory.get)
        min_weight = self.memory[min_edge]
        
        # Add the new edge to the spanning tree.
        node1, new_node = min_edge  # Unpack the new node from the edge tuple.
        edge_with_weight = min_edge + (min_weight,)  # Add the new weight (one-element-tuple,) to the edge tuple.
        self.storeSpanningTree(new_node, "Added node " + new_node + " to the spanning tree.", edge_with_weight)
        self.current_node = new_node
        
        return min_edge

    def exposeMemory(self):
        print("\nExposing agent's memory...")
        print("Memory of candidates for the next edge: ")
        for edge, weight in self.memory.items():
            node1, node2 = edge
            print("Edge from " + node1 + " to " + node2 + " with weight " + str(weight))
            
    ###################################################################################################
    # TASK 5: Implement a node-walking agent travelling the current spanning tree - in the making.
    # As it travels, it will expand the spanning tree in question.
    ###################################################################################################                
    def buildSpanningTreeAlongWalk(self):
        # While the spanning tree is not complete, keep building it.
        while len(self.spanning_tree_nodes) < len(self.graph.getNodes()):
            # Find the smallest edge from the current spanning tree to a new node.
            new_edge = self.choseNextEdgePrimAlgo()
            if new_edge is not None:
                # Let the agent walk to the new node and expand the spanning tree.
                self.current_node = new_edge[1]
            else:
                break


###################################################################################################
 # TEST FUNCTIONS
###################################################################################################
# # TASK 1: Create a graph with 6 nodes and add the edges to the graph.
print()
g = Graph()
for i in range(1, 7):
    g.addNode(Node('V' + str(i)))
    
# Add the following edges to the graph:
g.addEdge('V1', 'V2', 1)
g.addEdge('V1', 'V4', 3)
g.addEdge('V2', 'V3', 2)
g.addEdge('V2', 'V5', 7)
g.addEdge('V2', 'V6', 6)
g.addEdge('V3', 'V6', 4)
g.display()
print()
###################################################################################################
# Uncomment the following code to test the worksheet's tasks. One block at a time, of course :)
###################################################################################################
# # TASKS 2, 3: Regular agent
# agent = Agent(g, 'V1')
# agent.exposeSensoryInformation()
# # Chose the next edge wisely as per Prim's algorithm.
# new_chosen_edge = agent.choseNextEdgePrimAlgo()
# while new_chosen_edge is not None:
#     new_chosen_edge = agent.choseNextEdgePrimAlgo()
#     # agent.exposeSensoryInformation()  # Optionally see the agent's sensory information at each step.

# # Expose the agent's spanning tree
# agent.exposeSpanningTree()
# print()
###################################################################################################
# # TASK 4: Agent Memory
# agentMemory = Agent(g, 'V1')
# agentMemory.exposeSensoryInformation()
# # Chose the next edge wisely as per Prim's algorithm with memory.
# new_chosen_edge = agentMemory.choseNextEdgePrimAlgoWithMemory()
# while new_chosen_edge is not None:
#     new_chosen_edge = agentMemory.choseNextEdgePrimAlgoWithMemory()
#     # agentMemory.exposeMemory()  # Optionally see the agent's memory at each step.

# # Expose the agentMemory's spanning tree
# agentMemory.exposeSpanningTree()
# print()
###################################################################################################
# # TASK 5: AgentWalker (node-walking agent)
# agentWalker = Agent(g, 'V1')
# agentWalker.buildSpanningTreeAlongWalk()
# agentWalker.exposeSpanningTree()
# print()
###################################################################################################
# That's all, folks!