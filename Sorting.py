a=[1,5,6,8,2,7,1,8,5,9]
l= len(a)
for i in range(l):
  for j in range(i+1,l):
    if a[i]>a[j]:
       a[i],a[j]=a[j],a[i]  
print(a)    
a=[1,5,6,8,2,7,1,8,5,9]
l= len(a)
for i in range(l):
  for j in range(i+1,l):
    if a[i]>a[j]:
       a[i],a[j]=a[j],a[i]  
p=int(input("Enter the position" ))
if p>l:
   print("larger than no of elements")    
else:   
   print(a[p-1])
