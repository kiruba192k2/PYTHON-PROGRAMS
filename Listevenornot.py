print("Even Elements in a List")
List=[1,2,3,4,5,6,7,8]
for x in List:
    if(x%2 ==0) : 
        print(x)

print("Even List") 
a=[]
b=[]
n=int(input("no:")) 
for i in range (n):
    a.append(int(input()))

for i in a:    
        if i%2==0 and i not in b:
            b.append(i)
print(b)         
