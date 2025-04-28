import heapq

def prim(graph, start_node):
    mst = []
    visited = set()
    edges = [(0, start_node, start_node)]  # Cost, to_node, from_node
    heapq.heapify(edges)

    while edges:
        cost, to_node, from_node = heapq.heappop(edges)
        if to_node not in visited:
            visited.add(to_node)
            if from_node != to_node:  # Avoid adding the initial self-loop
                mst.append((from_node, to_node, cost))

            for neighbor, weight in graph[to_node].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, neighbor, to_node))
    return mst

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'C': 8, 'D': 6},
    'C': {'B': 8, 'E': 9},
    'D': {'A': 5, 'B': 6, 'E': 7},
    'E': {'C': 9, 'D': 7}
}

start_node = 'A'
mst = prim(graph, start_node)

print("Minimum Spanning Tree:")
for edge in mst:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")