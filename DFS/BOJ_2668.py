# 원형 연결리스트가 될 경우 result에 추가된다.
import sys
input = sys.stdin.readline

def dfs(a) :
    global result, linkArr
    b = arr[a-1]

    if b in linkArr :
        if b != linkArr[0] :
            # a가 현재 연결리스트에 있는데 시작노드가 아닐 경우 -> 결과가 될 수 없음
            return
        if b == linkArr[0] :
            # a가 현재 연결리스트에 있는데 시작노드일 경우 -> 결과에 추가됨
            result.extend(linkArr)
            return

    # a가 현재 연결리스트에 없을 경우 다음 노드로 넘어감
    linkArr.append(b)
    dfs(b)


# 입력
N = int(input().rstrip())
arr = []
result = []
linkArr = []

for _ in range(N) :
    arr.append(int(input().rstrip()))

# dfs 시행
for i in range(N) :
    # 해당 값이 결과리스트에 없는 경우만 시행(있는 경우는 이미 연결리스트로 판단된 것)
    if i not in result :
        linkArr = [i+1]
        dfs(i+1)

# 중복제거
result = list(set(result))
# 정렬
result.sort()

# 출력
print(len(result))
for x in result :
    print(x)