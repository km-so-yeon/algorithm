# 프로그래머스 42898
def solution(m, n, puddles):
    result = 0
    DP = []
    for _ in range(n + 1):
        DP.append([0] * (m + 1))

    DP[1][1] = 1
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                continue
            if [y, x] in puddles:
                DP[x][y] = 0
            else:
                DP[x][y] = DP[x - 1][y] + DP[x][y - 1]

    result = DP[n][m]
    return result % 1000000007