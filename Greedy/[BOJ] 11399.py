n = int(input())
hour_list = list(map(int, input().split()))
sum = 0
index = 0

hour_list.sort()

for hour in hour_list :
    sum += hour * (n - index)
    index += 1

print(sum)