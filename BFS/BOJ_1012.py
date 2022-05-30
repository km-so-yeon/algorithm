import sys
from collections import deque
input = sys.stdin.readline

# 1. BFS로 인접한 배추구역 파악
# 2. 인접한 배추구역 끝날 때마다 지렁이 수 + 1

def bfs(graph) :
    result = 0
    queue = deque()

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 1 :
                queue.append((i, j))
                graph[i][j] = 0

                while queue :
                    x, y = queue.popleft()

                    for d in range(4) :
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if nx < 0 or nx >= N or ny < 0 or ny >= M :
                            continue
                        if graph[nx][ny] == 1 :
                            queue.append((nx, ny))
                            graph[nx][ny] = 0

                result += 1

    print(result)

# 입력하기
caseCount = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 한 케이스마다 BFS 실행
for _ in range(caseCount) :
    N, M, K = map(int, input().split())

    graph = []
    for _ in range(N) :
        graph.append([0] * M)

    for _ in range(K) :
        x, y = map(int, input().split())
        graph[x][y] = 1

    bfs(graph)

