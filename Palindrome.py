n=int(input("no:")) 
org=n
rev=0
rem=0
while(n!=0):
    rem=n%10
    rev=rev*10 +rem
    n//=10
   
if(rev==org) :
    print("Yes")
else:
    print("No")