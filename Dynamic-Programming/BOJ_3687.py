num = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
minDP = [0] * 101
maxDP = [0] * 101

# n은 2 ~ 100
# n = 2일 때 최소값 1(2), 최대값 1(2)
# n = 3일 때 최소값 7(3), 최대값 7(3)
# n = 4일 때 최소값 4(4), 최대값 11(2 + 2)
# n = 5일 때 최소값 2(5), 최대값 71(3 + 2)
# n = 6일 때 최소값 6(6), 최대값 111(2 + 2 + 2)
# n = 7일 때 최소값 8(7), 최대값 711(3 + 2 + 2)
# n = 8일 때 최소값 10(2 + 6), 최대값 1111(2 + 2 + 2 + 2)
# n = 9일 때 최소값 18(2 + 7), 최대값 7111(3 + 2 + 2 + 2)
# n = 10일 때 최소값 22(5 + 5), 최대값 11111(2 + 2 + 2 + 2 + 2)
# n = 11일 때 최소값 20(5 + 6), 최대값 71111(3 + 2 + 2 + 2 + 2)
# n = 12일 때 최소값 28(5 + 7)
# n = 13일 때 최소값 68(6 + 7)
# n = 14일 때 최소값 88(7 + 7)
# n = 15일 때 최소값 108(8 + 7)
# n = 16일 때 최소값 188(9 + 7)


def findMin() :
    for n in range(2, 101) :
        # n이 2 ~ 7일 경우 : 해당 값이 있는 인덱스를 입력
        if n >= 2 and n <= 7 :
            minDP[n] = num.index(n) + 1
        # n이 그 이상의 값일 경우 : 뺐을 때 7 이하로 나오는 값 + 나머지 값
        else :
            cal = []
            for i in range(n - 7, n) :
                if i < 2 :
                    continue
                if n - i == 6 : # 남은 갯수가 6일 경우 뒤에 0을 붙이는 것이 최소값
                    cal.append(int(str(minDP[i]) + "0"))
                else :
                    cal.append(int(str(minDP[i]) + str(minDP[n - i])))
            minDP[n] = min(cal)

def findMax() :
    maxDP[2] = 1
    maxDP[3] = 7
    maxDP[4] = 11
    for n in range(5, 101) :
        maxDP[n] = int(str(maxDP[n - 2]) + "1")


caseNum = int(input())
findMin()
findMax()
for _ in range(caseNum):
    n = int(input())
    print("%d %d" % (minDP[n], maxDP[n]))