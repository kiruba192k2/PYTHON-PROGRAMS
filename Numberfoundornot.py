List=[1,2,3,4,5,6,7,8]
n= int(input("enter a number to search"))
for x in List:
    if(n==x):
        print("found")
        break
else:
    print("not found")

List=[1,2,3,4,5,6,7,8]
n= int(input("enter a number to search"))
l =len(List)
for i in range(l):
    if(List[i]==n):
           
        print("the given number is found in the position of" ,i+1)
        break
else:
    print("not found")
       

