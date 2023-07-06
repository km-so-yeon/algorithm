import sys
input = sys.stdin.readline

def maxProfit() :
    day = int(input().rstrip())
    stocks = list(map(int, input().split()))
    value = 0
    max = 0

    for i in range(len(stocks) - 1, -1, -1) :
        if(stocks[i] > max) :
            max = stocks[i]
        else :
            value += max - stocks[i]
    
    return value

N = int(input().rstrip())

for _ in range(N) :
    print(maxProfit())
