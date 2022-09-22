# 프로그래머스 최소직사각형
def solution(sizes):
    answer = 0
    resultX = 0
    resultY = 0

    for x, y in sizes:
        if x < y:
            resultX = max(resultX, x)
            resultY = max(resultY, y)
        else:
            resultX = max(resultX, y)
            resultY = max(resultY, x)

    answer = resultX * resultY

    return answer