import sys
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
arr = list(map(int, input().split()))
sum = [arr[0]]

# 현재의 값 혹은 합계 + 현재 값 중에서 더 큰 값을 추가한다.
for i in range(N - 1) :
    sum.append(max(sum[i] + arr[i + 1], arr[i + 1]))

print(max(sum))