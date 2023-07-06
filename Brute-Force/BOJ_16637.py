import sys
import copy
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(input().split())
maxValue = -100000000

# dfs로 수식을 계산한다
# index가 지나가면서 해당 연산자로 연산을 하거나 그대로 배열을 유지하거나 한다.
# index가 끝나고나서 배열에 남아있는 값들을 계산하고 최대값이면 max를 수정한다.

def dfs(expArr, idx, yn) :

    if idx == N :
        result = calArr(expArr)
        if result > maxValue :
            maxValue = result
        return

    # 숫자일 경우
    if(arr[idx].isdigit()) :
        dfs(expArr.append(arr[idx]), idx + 1, yn)
        return

    expArr1 = copy.deepcopy(expArr)
    expArr2 = copy.deepcopy(expArr)
    
    # 괄호를 사용했을 경우
    if(yn == False) :
        num = expArr1.pop()
        num = cal(num, arr[idx], arr[idx + 1])
        expArr1.append(num)
        dfs(expArr1, idx + 2, True)

    # 괄호를 사용하지 않았을 경우
    expArr2.append(arr[idx])
    expArr2.append(arr[idx + 1])
    dfs(expArr2, idx + 2, False)
    


def calArr(arr) :
    result = arr[0]
    
    for i in range(len(arr)) :
        op = arr[i]
        if op == '+' :
            result = result + arr[i + 1]
        if op == '-' :
            result = result - arr[i + 1]
        if op == '*' :
            result = result * arr[i + 1]

    return result

def cal(num1, op, num2) :
    if op == '+' :
        return num1 + num2
    if op == '-' :
        return num1 - num2
    if op == '*' :
        return num1 * num2
