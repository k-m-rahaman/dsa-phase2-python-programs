from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

visited = set()
queue = deque([0])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(graph[node])