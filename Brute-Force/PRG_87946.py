# 프로그래머스 피로도
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    N = len(dungeons)

    for order in permutations(range(N), N):
        cnt = 0
        have = k
        for i in order:
            if dungeons[i][0] <= have:
                cnt += 1
                have -= dungeons[i][1]
            else:
                break;

        answer = max(answer, cnt)

    return answer