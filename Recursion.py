a=int(input("Number of elements in the array:-"))
n=list(map(int, input("elements of array:-").split()))
total=int(input())
n.sort()
n.sort(reverse=True)
comb=[]
i=0
def recursion(total,i,comb):
    if total==0:
        return comb 
    if i<a:
        if total>=n[i]:
            total=total-n[i]
            comb.append(n[i])
        else:
            i+=1
    return recursion(total,i,comb)
recursion(total,i,comb)
print(comb)
     
