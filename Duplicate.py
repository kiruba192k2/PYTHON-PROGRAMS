a=[1,2,3,4,1,2,3,4,2]
l = len(a)
x= False
for i in range(l):
    for j in range(i+1,l):
        if(a[i]==a[j] ):
            print(a[i])
            x=True
            break
    if x:
        break      

a=[1,2,3,4,1,2,3,4,2]

for i in a:
    if a.count(i)>1:
        print(i)
        break

a=[1,2,3,4,5,1]
b=[]
 
for i in a:
    if i in b:
        print(i)
        break
    b.append(i)

b=[]
for i in [1,2,3,4,5,2]:
    if i in b:
        print(i)
        break
    b.append(i)
else:print("no duplicates found")

for i in range (10):
  print(i)    