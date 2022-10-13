import sys
input = sys.stdin.readline

# 맵을 돌면서 방문안했고 집이 있으면 DFS 실행
# DFS돌면서 몇집이 있는지 count하기
# DFS끝나고 나면 count한 것을 리스트에 넣기

def dfs(x, y) :
    global count

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N :
            continue
        # 방문한 적 없고 집이 있으면 진행
        if visit[ny][nx] == 0 and arr[ny][nx] == 1 :
            count += 1
            visit[ny][nx] = 1
            dfs(nx, ny)

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#입력
N = int(input())
arr = [[] for _ in range(N)]
visit = [[0] * N for _ in range(N)]
count = 0
result = []

for i in range(N) :
    line = input()
    for j in range(N) :
        arr[i].append(int(line[j]))

for y in range(N) :
    for x in range(N) :
        if arr[y][x] == 1 and visit[y][x] == 0 :
            count = 1
            visit[y][x] = 1
            dfs(x, y)
            result.append(count)

result.sort()

print(len(result))
for x in result :
    print(x)