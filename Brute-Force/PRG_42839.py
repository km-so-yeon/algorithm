from itertools import permutations

#프로그래머스 소수 찾기
def solution(numbers):
    num = [n for n in numbers]
    per = []
    perNum = []
    prime = []

    # n개의 숫자가 있을 경우 1 ~ n자릿수의 숫자가 만들어질 수 있다.
    # n자릿수의 숫자 : numbers에서 n개를 뽑은 순열
    for i in range(1, len(numbers) + 1):
        per += list(permutations(num, i))
    perNum = [int("".join(p)) for p in per]

    for n in perNum:
        if n < 2:
            continue
        check = True
        for i in range(2, int(n ** 0.5) + 1):  # n의 제곱근보다 작은 숫자까지만 나눗셈
            if n % i == 0:
                check = False
                break
        if check:
            prime.append(n)

    return len(set(prime))