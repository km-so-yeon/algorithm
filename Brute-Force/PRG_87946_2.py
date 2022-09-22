answer = 0
N = 0
visited = []

def dfs(have, cnt, dungeons) :
    global answer
    answer = max(answer, cnt)

    for i in range(N) :
        if have >= dungeons[i][0] and not visited[i] :
            visited[i] = 1
            dfs(have - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N

    dfs(k, 0, dungeons)

    return answer