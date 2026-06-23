a=[]
n=int(input("no:")) 
for i in range (n):
    a.append(int(input()))
no=int(input("enter a no to search:"))
j =0
for i in a:
    j=j+1
    if(no==i):
        j=j+1
        print("the number",no,"is present in the index of ",j)       
    else:
       print("the number",no,"isn't present")