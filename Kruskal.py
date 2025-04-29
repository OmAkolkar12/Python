def kruskal(edges, n):
    parent = [i for i in range(n)]

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    mst_edges = []
    mst_cost = 0

    edges.sort()  # Sort edges by weight

    for weight, u, v in edges:
        if find(u) != find(v):
            mst_cost += weight
            mst_edges.append((u, v, weight))
            parent[find(u)] = find(v)

    print("\nEdges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} -- {v}  (weight {weight})")

    print("\nTotal cost of MST:", mst_cost)


def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    edges = []

    print("\nEnter edges as (u v weight):")
    for _ in range(e):
        u, v, weight = map(int, input().split())
        edges.append((weight, u, v))  # Store as (weight, u, v) for easy sorting

    kruskal(edges, n)


if __name__ == "__main__":
    main()
