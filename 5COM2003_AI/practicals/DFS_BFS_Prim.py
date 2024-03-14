# 5COM2003_AI
# DFS, BFS, Prim theory
# Examples from lecture 

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}  # Dictionary < name: weight >
        
    def addAdjacentNode(self, neighbour, weight):
        self.adjacent[neighbour] = weight
    
    def getAdjacentNodes(self):
        return self.adjacent   
    
    # Neatly display the actual node and its adjacent nodes.
    def display(self):
        print(self.name)
        for neighbour, weight in self.adjacent.items():
            print(f'  {neighbour.name} - {weight}')
        print()


class Graph:
    def __init__(self):
        self.nodes = []
    
    def addNode(self, node):
        self.nodes.append(node)
    
    def display(self):
        print("Graph:")
        for node in self.nodes:
            node.display()

    

# Create a graph
graph = Graph()

v1 = Node('V1')
v2 = Node('V2')
v3 = Node('V3')
v4 = Node('V4')
v5 = Node('V5')
v6 = Node('V6')
v1.addAdjacentNode(v2, 1)
v1.addAdjacentNode(v4, 3)
v2.addAdjacentNode(v3, 2)
v2.addAdjacentNode(v5, 7)
v2.addAdjacentNode(v6, 6)
v3.addAdjacentNode(v6, 4)
v4.addAdjacentNode(v1, 3)
v5.addAdjacentNode(v2, 7)
v6.addAdjacentNode(v2, 6)
v6.addAdjacentNode(v3, 4)

# Add nodes to the graph
graph.addNode(v1)
graph.addNode(v2)
graph.addNode(v3)
graph.addNode(v4)
graph.addNode(v5)
graph.addNode(v6)

# Display the graph
graph.display()

# Depth First Search
def dfs(graph, start, visited):
    print(start.name)
    visited.add(start)
    for neighbour, weight in start.getAdjacentNodes().items():
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    if visited == set(graph.nodes):
        print("All nodes visited.")
           
print("DFS: ")
dfs(graph, v1, set())


# Breadth First Search
def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        current = queue.pop(0)  # Remove the first element from the queue (FIFO).
        print(current.name)
        for neighbour, weight in current.getAdjacentNodes().items():
            if neighbour not in visited:
                queue.append(neighbour)  # Add the neighbour to the queue.
                visited.add(neighbour)  # Mark the neighbour as visited and add it to the set.
    if visited == set(graph.nodes):
        print("All nodes visited.")

print("\nBFS: ")
bfs(graph, v1)

# Prim's Algorithm to find the minimum spanning tree using minheap
import heapq  
# A heap is a binary tree that satisfies the heap property. The heap property is as follows: 
# In a min heap, for every node x with parent p, the key of p is less than or equal to the key of x.

def prim(graph, start):
    visited = set()
    mst = []
    queue = [(0, start, None)]  # (weight, node, parent)
    while queue:
        weight, current, parent = heapq.heappop(queue)  # Remove the smallest element from the queue.
        if current not in visited:  # Ensure no cycles are formed.
            visited.add(current)
            if parent is not None:
                mst.append((parent, current, weight))
            for neighbour, weight in current.getAdjacentNodes().items():
                if neighbour not in visited:
                    heapq.heappush(queue, (weight, neighbour, current))  # Add the neighbour to the queue.
    return mst

print("\nPrim's Algorithm: ")
mst = prim(graph, v1)
print("Minimum Spanning Tree:")
for edge in mst:
    print(f'{edge[0].name} - {edge[1].name} : {edge[2]}')


