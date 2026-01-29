import random
l = [random.randint(1,1000) for _ in range(10)]
n=len(l)
for i in range(1,n):
    j=i-1
    v=l[i]
    while j>=0 and l[j]>v:
        l[j+1] = l[j]
        j=j-1
    l[j+1]=v

print(l)
    
        
