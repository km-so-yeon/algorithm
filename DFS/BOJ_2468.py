import sys
import copy
input = sys.stdin.readline

# 1. 최소 높이부터 최대 높이까지 DFS로 인접한 안전구역 파악
# 2. 인접한 안전구역 끝날 때마다 안전구역 개수 + 1
# 3. 안전구역 개수 중 최대값을 출력

def countArea(copy_graph, h) :
    count = 0
    for i in range(N) :
        for j in range(N) :
            if copy_graph[i][j] > h :
                dfs(copy_graph, h, i, j)
                count += 1

    return count

def dfs(copy_graph, h, i, j) :
    copy_graph[i][j] = 0

    for d in range(4) :
        nx = i + dx[d]
        ny = j + dy[d]

        if nx < 0 or nx >= N or ny < 0 or ny >= N :
            continue
        if copy_graph[nx][ny] > h :
            copy_graph[nx][ny] = 0
            dfs(copy_graph, h, nx, ny)

graph = []
N = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = 0
for _ in range(N) :
    graph.append(list(map(int, input().split())))

MIN = min(map(min, graph))
MAX = max(map(max, graph))

for h in range(MIN, MAX) :
    copy_graph = copy.deepcopy(graph)
    count = countArea(copy_graph, h)
    if count > result :
        result = count

print(result)