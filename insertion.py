l=[2,5,3,8,4]
print(l)
n=len(l)
for i in range(1,n):
    j=i-1
    v=l[i]
    while j>=0 and l[j]>v:
        l[j+1] = l[j]
        j=j-1
    l[j+1]=v

print(l)
    
        
