



def all_shortest_paths(self, start, end):
    # Initialize the BFS queue with the start node and a path containing only the start node
    queue = deque([(start, [start.get_name()])])
    visited = set()
    shortest_paths = []
    shortest_length = float('inf')

    while queue:
        current_node, path = queue.popleft()
        if current_node not in visited or len(path) <= shortest_length:
            visited.add(current_node)
            # If the current node is the end node, add the path to the shortest_paths
            if current_node == end:
                shortest_length = len(path)
                shortest_paths.append(path)
            # Extend the path to the neighbors not yet visited
            for neighbor in current_node.get_neighbours():
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor.get_name()]))

    # Return only the shortest paths from the collected paths
    return [p for p in shortest_paths if len(p) == shortest_length]

def betweenness_centrality(self, node):
    betweenness = 0
    for s in self.graph.get_nodes().values():
        for t in self.graph.get_nodes().values():
            if s != t and s != node and t != node:
                # Compute all shortest paths from s to t using a modified BFS
                all_paths = self.all_shortest_paths(s, t)
                shortest_paths_through_v = [path for path in all_paths if node.get_name() in path]
                betweenness += len(shortest_paths_through_v) / len(all_paths) if all_paths else 0
    print(f"- {node.get_name()} Betweenness Centrality = {betweenness}")