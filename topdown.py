Total = 11
coins = [1,2,5]
ans = []
while(Total>0):
    temp = []
    for i in coins:
        t = Total-i
        if t>=0:
            temp.append(Total-i)
    minimum = temp.index(min(temp))
    output.append(coins[minimum])
    Total=temp[minimum]
print(output)
