from collections import deque
import sys
input = sys.stdin.readline

# 미로에서 상하좌우 돌아다니면서 갈 수 있는 길을 찾는다.
# 최단거리는 BFS (DFS는 지나갈 수 있는 길을 모두 찾고 가장 작은값을 선택해야해서 시간복잡도가 커진다.)
# 길을 찾으면서 현재 자리에 지나왔던 칸 수 + 1를 입력한다.
# maze[y][x] maze[N][M]

def bfs() :
    global check
    queue = deque()
    queue.append((0, 0))
    check[0][0] = 1
    visit[0][0] = 1

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 밖으로 나가게되면 넘어가기
            if nx < 0 or ny < 0 or nx >= M or ny >= N :
                continue

            # 길이 있고, 방문하지 않았을 경우 큐에 넣기
            if maze[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                check[ny][nx] = check[y][x] + 1
                queue.append((nx, ny))

#입력
#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
check = [[0] * M for _ in range(N)]     #이동한 칸의 수
visit = [[0] * M for _ in range(N)]     #방문했는지 여부
maze = [[] for _ in range(N)]

for i in range(N) :
    arr = input().rstrip()
    for j in range(M) :
        maze[i].append(int(arr[j]))

#미로찾기
bfs()
print(check[N - 1][M - 1])