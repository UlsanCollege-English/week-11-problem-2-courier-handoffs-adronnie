"""
HW02 — Courier Handoffs (BFS Shortest Path)

Implement:
- bfs_path(graph, s, t)
"""

from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.
    """
    # Step 1: check if nodes exist
    if s not in graph or t not in graph:
        return None

    # Step 2: trivial case
    if s == t:
        return [s]

    # Step 3: initialize BFS
    queue = deque([s])
    visited = set([s])
    parent = {}  # child -> parent

    # Step 4: BFS loop
    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)
                if v == t:  # found target
                    # Step 5: reconstruct path
                    path = [t]
                    while path[-1] != s:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path

    # Step 6: target not found
    return None


if __name__ == "__main__":
    # Optional manual test
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    print(bfs_path(sample_graph, 'A', 'E'))  # Example: ['A', 'B', 'D', 'E']
    print(bfs_path(sample_graph, 'A', 'A'))  # ['A']
    print(bfs_path(sample_graph, 'A', 'Z'))  # None
