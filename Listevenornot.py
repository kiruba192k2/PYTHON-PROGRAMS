List=[1,2,3,4,5,6,7,8]
for x in List:
    if(x%2 ==0) : 
        print(x)

a=[]
n=int(input("no:")) 
for i in range (n):
    a.append(int(input()))
b=[]
for i in a:    
        if i%2==0 and i not in b:
            b.append(i)
print(b)         
