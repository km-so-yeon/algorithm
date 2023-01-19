import sys
from collections import deque
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
arr = list(map(int, input().split()))
op = input().split()
opQueue = deque()
result = []

for i in range(op.length) :
    for j in range(op[i]) :
        if i == 0 :
            opQueue.append('+')
        elif i == 1 :
            opQueue.append('-')
        elif i == 2 :
            opQueue.append("*")
        elif i == 3 :
            opQueue.append("/")

# 연산자를 숫자 사이사이에 배치해가며 결과값을 저장
def dfs(count, value) :
    if count == N :
        result.append(value)

