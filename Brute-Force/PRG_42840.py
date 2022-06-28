def solution(answers):
    # 수포자 삼인방이 답을 찍는 방식
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    # 채점
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            score[0] += 1
        if answers[i] == p2[i % len(p2)]:
            score[1] += 1
        if answers[i] == p3[i % len(p3)]:
            score[2] += 1

    # 가장 많이 맞춘 사람 찾기
    maxScore = max(score)
    for i in range(3):
        if score[i] == maxScore:
            result.append(i + 1)

    return result