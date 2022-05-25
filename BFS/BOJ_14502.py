import sys
from collections import deque
import copy
input = sys.stdin.readline

# 1. 벽을 세우기
# 2. 3개째 세웠을 때 BFS 수행
# 3. BFS로 바이러스를 퍼트려서 안전영역의 최대 크기 구하기

def makeWall(count) :
    if count == 3 :
        bfs()
        return

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 0 :
                graph[i][j] = 1
                makeWall(count + 1)
                graph[i][j] = 0

def bfs() :
    # 바이러스가 있는 위치를 가지고 있는 큐
    queue = deque()
    # 벽 3개를 세울 때마다 바이러스가 퍼지는 위치가 다르기 때문에 사용
    copy_graph = copy.deepcopy(graph)

    for i in range(N) :
        for j in range(M) :
            if copy_graph[i][j] == 2 :
                queue.append((i, j))

    # 바이러스를 퍼트린다
    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if copy_graph[nx][ny] == 0 :
                copy_graph[nx][ny] = 2
                queue.append((nx, ny))

    # 안전구역 count
    global result
    count = 0
    for i in range(N) :
        count += copy_graph[i].count(0)

    result = max(result, count)

# 입력받기
graph = []
N, M = map(int, input().split())
result = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(N) :
    graph.append(list(map(int, input().split())))

makeWall(0)
print(result)