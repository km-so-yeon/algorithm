import sys

input = sys.stdin.readline

cnt = 0


def subset_sum(idx, result):
    global cnt

    if idx >= N:
        return

    result += arr[idx]

    if result == S:
        cnt += 1

    # 현재 숫자를 선택한 경우
    subset_sum(idx + 1, result)

    # 현재 숫자를 선택하지 않은 경우
    subset_sum(idx + 1, result - arr[idx])


N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

subset_sum(0, 0)

print(cnt)
