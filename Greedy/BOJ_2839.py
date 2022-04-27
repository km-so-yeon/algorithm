weight = int(input())
count = 0

while weight > 0 :
    if weight >= 3 and (weight % 5 != 0) :
        weight -= 3
        count += 1
    elif weight >= 5 :
        weight -= 5
        count += 1
    else :
        count = -1
        break;


print(count)
