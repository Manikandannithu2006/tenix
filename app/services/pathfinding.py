import heapq

def astar(graph, start, goal):
    if start not in graph or goal not in graph:
        return []

    pq = [(0, start)]
    visited = set()
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            break

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                heapq.heappush(pq, (0, neighbor))

    if goal not in parent:
        return []

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    return path[::-1]