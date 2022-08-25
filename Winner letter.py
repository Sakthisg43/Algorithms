letters = ['a','b','c','d','e','f','g','h','i','j','k']
count1= 1
n=len(letters)
i=0
while(letters.count('-')<n-1):
    if i==n:
        i=0
    if letters[i]!='-':
        if count1%4==0 or count1%10==4:
            count1+=1
            letters[i]='-' 
        if letters[i]!='-':
            count1+=1
    i+=1
for j in letters:
    if j!='-':
        print(f"The Winner letter is ->  '{j}'")
