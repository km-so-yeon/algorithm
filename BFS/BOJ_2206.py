import sys
from collections import deque
input = sys.stdin.readline
# BFS로 탐색하면서
# 탐색하면서 한번만 통과 가능

def bfs() :
    q = deque()
    q.append((0, 0, 1, 0)) #x, y, 몇번째 방문인지, 통과여부(이미 했음->불가능일 경우 1, 아니면 0)

    while q :
        x, y, n, yn = q.popleft()

        if x == M-1 and y == N-1 :
            return n

        # 상하좌우 추가
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 넘어가면 pass
            if nx < 0 or ny < 0 or nx >= M or ny >= N :
                continue

            # 벽일 경우
            if map[ny][nx] == '1' :
                if yn == 1 :
                    continue
                # 처음 한번은 벽 통과
                else :
                    q.append((nx, ny, n + 1, 1))
                    continue

            q.append((nx, ny, n + 1, yn))

    # 성공하지 못했을 경우
    return -1

# 입력
# 세로, 가로
N, M = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
map = []

for i in range(N) :
    map.append(input().rstrip())

print(bfs())