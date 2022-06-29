# 퀸은 서로 같은 세로줄, 가로줄에 있을 수 없기 때문에 일차원 배열로 좌표값을 관리한다. `row[x] = y`은 퀸이 (x, y) 좌표에 있는 것
# 1. x값을 0부터 n까지 +1 할 때마다 y값을 0부터 n까지 +1씩 해본다.
# 2. y좌표값을 옮길 때마다 같은 세로, 가로줄에 있는지, 대각선에 있다면 이전으로 다시 되돌아가고 아닐 경우 다음 x좌표로 넘어간다.
# 3. 퀸이 모두 놓였을 때(모든 세로줄에 퀸이 하나씩 있을 때, x값이 n값이 될 때) 경우의 수에 +1을 하고 해당 경우를 끝낸다.

def n_queen(x) :
    global result
    if x == n :
        result += 1
        return

    for y in range(n) :
        row[x] = y
        if promising(x) :
            # 서로 공격하는 위치가 아닌 경우 다음 x좌표로 넘어간다.
            n_queen(x + 1)

# 유망한지 판단하는 함수
def promising(x) :
    # 가로줄에 있는지(이 전까지 있었던 좌표값들과 같은 y값을 가지는지), 대각선에 있는지(x값끼리 뺀 값과 y값끼리 뺀 값의 절대값이 같은지) 체크
    for i in range(x) :
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]) :
            return False

    return True

result = 0
n = int(input())
row = [0] * n
n_queen(0)
print(result)