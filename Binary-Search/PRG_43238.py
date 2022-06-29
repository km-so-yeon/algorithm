def solution(n, times):
    # 이분 탐색 할 값 : 모든 사람이 심사를 받는데 걸리는 시간
    # 초기 설정 범위 : 최소값은 1이고, 최대값은 가장 오래 걸리는 심사대에서 모든 사람이 받는 시간
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            # people은 심사받은 사람 수
            people += mid // time

            # 모든 심사관에게 심사받지 않아도 모든 사람이 심사를 받은 경우
            if people >= n:
                break

        # 모든 심사관에게 심사를 받은 경우 최대값을 중간값 - 1로 설정
        # 새로 설정된 범위 : 최소값 ~ (중간값 - 1)
        if people >= n:
            answer = mid
            right = mid - 1
        # 모든 심사관에게 심사를 받지 못한 경우 최소값을 중간값 + 1로 설정
        # 새로 설정된 범위 : (중간값 + 1) ~ 최대값
        else:
            left = mid + 1

    return answer