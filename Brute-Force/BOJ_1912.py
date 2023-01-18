import sys
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
arr = list(map(int, input().split()))
result = []

# 모든 구간의 합을 구한다
for i in range(N) :
    value = 0
    for j in range(i, N) :
        value += arr[j]
        result.append(value)

# 모든 구간의 합 중에서 최대값
print(max(result))