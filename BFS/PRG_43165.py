# 프로그래머스 타겟 넘버
from collections import deque

def solution(numbers, target):
    answer = 0

    def dfs(idx, result):
        nonlocal answer
        if idx == len(numbers):
            if result == target:
                answer += 1
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    # dfs(0, 0)

    def bfs():
        nonlocal answer
        queue = deque()
        queue.append([numbers[0], 0])
        queue.append([-1 * numbers[0], 0])

        while queue:
            num, idx = queue.popleft()
            if idx == len(numbers) - 1:
                if num == target:
                    answer += 1
            else:
                queue.append([num + numbers[idx + 1], idx + 1])
                queue.append([num - numbers[idx + 1], idx + 1])

    bfs()

    return answer