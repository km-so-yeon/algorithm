import sys
input = sys.stdin.readline

graph = []
nodeCount = int(input())
lineCount = int(input())

def dfs(graph, v, visited) :
    visited[v] = True

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

for _ in range(nodeCount + 1) :
    graph.append(list())

for _ in range(lineCount) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (nodeCount + 1)
wormCount = 0

dfs(graph, 1, visited)

for v in visited :
    if v :
        wormCount += 1

print(wormCount - 1)

