graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

dfs(0)