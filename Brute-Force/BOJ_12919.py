import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
result = 0

# t에서 규칙대로 문자열을 줄여가면서 s가 나오면 1, 안되면 0



def dfs(curStr) :

    global result

    if s == curStr :
        result = 1

    if len(curStr) == 0 :
        return

    # 1번 규칙 -> 문자열 맨뒤가 A라면 A 삭제하기
    if curStr[-1] == 'A' :
        dfs(curStr[:-1])

    # 2번 규칙 -> 문자열 맨 앞이 B라면 B제거하고 뒤집기
    if curStr[0] == 'B' :
        dfs(curStr[-1:0:-1])
    

dfs(t)

print(result)
