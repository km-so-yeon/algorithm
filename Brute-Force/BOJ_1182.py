import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

# dfs를 하면서 S가 되면 count에 추가한다

def dfs(sum, idx) :
    global count

    if idx >= N :
        return

    sum += nums[idx]

    if(sum == S) :
        count += 1

    # 현재 인덱스의 값을 추가했을 때
    dfs(sum, idx + 1)

    # 현재 인덱스의 값을 추가하지 않았을 때
    dfs(sum - nums[idx], idx + 1)


dfs(0, 0)

print(count)
