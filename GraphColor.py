def is_safe(node, graph, color, c):
    # Check if any adjacent node has the same color
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, m, color, node):
    if node == len(graph):
        return True  # All nodes colored successfully

    for c in range(1, m+1):
        if is_safe(node, graph, color, c):
            color[node] = c  # Assign color
            if graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0  # Backtrack

    return False  # No color can be assigned

def main():
    # Example Graph as adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    n = len(graph)  # Number of nodes
    m = 3           # Number of colors allowed (you can change it)
    
    color = [0] * n  # Initially no color assigned

    if graph_coloring(graph, m, color, 0):
        print("Solution exists:")
        for node in range(n):
            print(f"Node {node} ---> Color {color[node]}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()