#프로그래머스 카펫
def solution(brown, yellow):
    answer = []
    size = []
    count = brown + yellow

    for i in range(2, count) :
        x = count // i
        y = i
        # 가능한 카펫 사이즈 구하기 -> yellow 는 전체 크기의 가로세로 -2
        if count % i == 0 and x >= y and (x - 2) * (y - 2) == yellow :
            return [x, y]