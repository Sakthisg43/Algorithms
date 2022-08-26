coins=[1,2,5]
amt=7
comb=[]
for x in range(0,amt+1):
    arr.append(amt+1)
arr[0]=0
for y in range(1,amt+1):
    mini=arr[y]
    for z in range(len(coins)):
        c=1
        t=y-coins[z]
        if t>0:
            c+=arr[t]
        if c<mini and t>=0:
            mini=c
    arr[y]=mini
print(arr[amt])
print(arr)
