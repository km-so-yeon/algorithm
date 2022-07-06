# 프로그래머스 정수 삼각형
import copy

def solution(triangle):
    copyTri = copy.deepcopy(triangle)

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            for k in range(2):
                if copyTri[i + 1][j + k] < triangle[i + 1][j + k] + copyTri[i][j]:
                    copyTri[i + 1][j + k] = triangle[i + 1][j + k] + copyTri[i][j]

    return max(copyTri[-1])