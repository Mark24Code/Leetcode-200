price = [7, 1, 5, 3, 6, 4]

if len(price) == 0:
    print(0)
else:
    minP = price[0]
    maxG = 0
    i = 0
    for i in range(0, len(price)):
        if price[i] < minP:
            minP = price[i]
        else:
            if price[i] - minP > maxG:
                maxG = price[i] - minP
    print(maxG)