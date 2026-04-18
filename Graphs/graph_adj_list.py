graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

for node in graph:
    print(node, "->", graph[node])