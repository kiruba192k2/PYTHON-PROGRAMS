a=[1,2,3,4,1]
b=[]
l = len(a)
for i in range(l):
    for j in range(i+1,l):
        if(a[i]==a[j]  and a[i] not in b):
            b.append(a[i])
print(b) 