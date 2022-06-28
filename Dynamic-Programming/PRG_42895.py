def solution(N, number):
    # 사용횟수 1일 때 결과값 : N
    # 사용횟수 2일 때 결과값 : NN, N+N, N-N, N/N
    # 사용횟수 3일 때 결과값 : NNN, (1일 때 결과값) 연산 (2일 때 결과값), (2일 때 결과값) 연산 (1일 때 결과값)
    # 사용횟수 4일 때 결과값 : NNNN, 1SET 연산 3SET, 2SET 연산 2SET, 3SET 연산 1SET
    # .. 사용횟수 1 ~ 8까지 계산하면서 number가 나올 경우 사용횟수 return
    # DP index가 0부터 시작하므로 x도 (사용횟수 - 1)부터 시작, y는 (사용횟수 - (x + 1) - 1)

    result = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[i - j - 2]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            result = i
            break;

        DP.append(numbers)

    return result