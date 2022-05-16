from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, v, visited) :
    # 현재 노드 방문 처리
    visited[v] = True;
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited) :
    # 큐 구현
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end=' ')

    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()

        # 해당 원소와 연결된, 미처 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                print(i, end=' ')

nodeCount, lineCount, start = map(int, input().split())
graph = []

for i in range(nodeCount + 1) :
    graph.append(list())

for i in range(lineCount) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(nodeCount + 1) :
    graph[i].sort()

dfs(graph, start, [False] * (nodeCount + 1))

print()

bfs(graph, start, [False] * (nodeCount + 1))