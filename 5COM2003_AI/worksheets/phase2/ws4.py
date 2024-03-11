class Agent:
    def __init__(self):
        # Initialize the agent's data structures
        self.spanning_tree_nodes = set()  # Set to store the nodes in the spanning tree
        self.spanning_tree_edges = set()  # Set to store the edges in the spanning tree
        self.memory = {'nodes': set(), 'edges': set()}  # Dictionary to store the agent's memory

    def add_to_spanning_tree(self, node, edge):
        # Add a node and edge to the spanning tree
        self.spanning_tree_nodes.add(node)  # Add the node to the spanning tree
        self.spanning_tree_nodes.add(edge[0])  # Add the edge's first node to the spanning tree
        self.spanning_tree_nodes.add(edge[1])  # Add the edge's second node to the spanning tree
        self.spanning_tree_edges.add(edge)  # Add the edge to the spanning tree

    def get_spanning_tree_nodes(self):
        # Get the nodes in the spanning tree
        return self.spanning_tree_nodes

    def get_spanning_tree_edges(self):
        # Get the edges in the spanning tree
        return self.spanning_tree_edges

    def sense_current_node(self, current_node):
        # Sense the current node
        return current_node

    def sense_edges_leaving_node(self, current_node, graph):
        # Sense the edges leaving the current node in the graph
        return graph[current_node] # Square brackets to access the list of edges leaving the current node

def choose_edge(agent, graph):
    # Choose the edge with the minimum weight that connects a node in the spanning tree
    # with a node outside the spanning tree
    min_weight = float('inf')
    min_edge = None

    for node in agent.get_spanning_tree_nodes():
        edges = agent.sense_edges_leaving_node(node, graph)
        for edge in edges:
            if edge[0] not in agent.get_spanning_tree_nodes() or edge[1] not in agent.get_spanning_tree_nodes():
                weight = edge[1]
                if weight < min_weight:
                    min_weight = weight
                    min_edge = (node, edge[0]) if edge[1] == weight else (node, edge[1])

    return min_edge

def dfs(agent, graph, start_node):
    # Perform Depth-First Search (DFS) starting from the given start_node
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in agent.get_spanning_tree_nodes():
            agent.sense_current_node(current_node)
            edges_leaving_node = agent.sense_edges_leaving_node(current_node, graph)
            chosen_edge = choose_edge(agent, graph)
            if chosen_edge:
                agent.add_to_spanning_tree(current_node, chosen_edge)
                next_node = chosen_edge[1] if chosen_edge[0] == current_node else chosen_edge[0]
                stack.append(next_node)

def main():
    # Graph representation
    graph = {
        'A': [('B', 2), ('C', 4)],
        'B': [('A', 2), ('D', 3), ('E', 1)],
        'C': [('A', 4), ('D', 5)],
        'D': [('B', 3), ('C', 5), ('E', 6)],
        'E': [('B', 1), ('D', 6)]
    }

    # Initialize agent
    agent = Agent()

    # Start DFS from node A
    dfs(agent, graph, 'A')

    # Print spanning tree nodes and edges
    print("Spanning Tree Nodes:", list(agent.get_spanning_tree_nodes()))
    print("Spanning Tree Edges:", list(agent.get_spanning_tree_edges()))
    
    print()
    print(agent.sense_current_node('A'))
    print(agent.sense_edges_leaving_node('A', graph))
    print("Agent memory: " , agent.memory)
    
    print(graph)

if __name__ == "__main__":
    main() 