# 1부터 9까지 직접 대입해보면서
# 해당 부등호가 성립하는지 확인하기

import sys
input = sys.stdin.readline

k = int(input())
signArr = input().split()
numArr = [0] * k
minNum = 999999999
maxNum = 0

for i in range(k) :
    num = 0

    if i == k - 1 :
        if num < minNum :
            minNum = num
        if num > maxNum :
            maxNum = num

print(numArr)