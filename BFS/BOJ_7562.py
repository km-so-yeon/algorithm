from collections import deque

def chess() :
    size = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    board = [[0] * size for _ in range(size)]

    #BFS
    queue = deque()
    queue.append((x1, y1))

    while queue :
        x, y = queue.popleft()

        # 이동하려고하는 칸에 도착했을 경우
        if x == x2 and y == y2 :
            print(board[x][y])
            break

        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= size or ny >= size :
                continue

            # 방문하지 않았을 경우 큐에 넣기
            if board[nx][ny] == 0 :
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

#테스트케이스 개수
caseCount = int(input())

#나이트가 이동하는 칸
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for _ in range(caseCount) :
    chess()