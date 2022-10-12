import sys
input = sys.stdin.readline

# 1일 때 1
# 2일 때 1경우의수 + 1, 1 + 1 = 2
# 3일 때 2경우의수 + 1, 1경우의수 + 2, 1 + 2 + 1 = 4
# 4일 때 3경우의수 + 1, 2경우의수 + 2, 1경우의수 + 3, 4 + 2 + 1 = 7
# 5일 때 4경우의수 + 1, 3경우의수 + 2, 2경우의수 + 1, 7 + 4 + 2 = 13

DP = [0, 1, 2, 4]

N = int(input());
arr = []

for n in range(N) :
    arr.append(int(input()))

for i in range(4, max(arr) + 1) :
    DP.insert(i, DP[i-1] + DP[i-2] + DP[i-3])

for a in arr :
    print(DP[a])