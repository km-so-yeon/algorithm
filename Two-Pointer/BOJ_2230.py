import sys
input = sys.stdin.readline

MAX = 20000000000

n, m = map(int, input().split())
arr = []
result = MAX

for i in range(n) :
    arr.append(int(input()));

arr.sort()
start, end = 0, 1

# 하나의 반복문 안에서 start와 end가 조정될 수 있도록 하기
while start < n and end < n :
    diff = arr[end] - arr[start]
    if diff == m :
        result = diff
        break
    elif diff < m :
        end += 1
    else :
        start += 1
        result = min(result, diff)

print(result)