# f = int(input("enter a Start value: "))
# if (f%2==0):
#     s=f
# else:
#     s=f+1
# e = int(input("enter a end value: "))
# print(*range(s, e+1, 2))
 


#duplicate number
# a=[1,2,3,4,1]
# b=[]
# l = len(a)
# for i in range(l):
#     for j in range(i+1,l):
#         if(a[i]==a[j]  and a[i] not in b):
#             b.append(a[i])
# print(b) 
       
#even number from list
# a=[]
# n=int(input("no:")) 
# for i in range (n):
#     a.append(int(input()))
# b=[]
# for i in a:    
#         if i%2==0 and i not in b:
#             b.append(i)
# # print(b) 
# sorting  
# a=[1,5,6,8,2,7,1,8,5,9]
# l= len(a)
# for i in range(l):
#   for j in range(i+1,l):
#     if a[i]>a[j]:
#        a[i],a[j]=a[j],a[i]  
# print(a)    
# a=[1,5,6,8,2,7,1,8,5,9]
# l= len(a)
# for i in range(l):
#   for j in range(i+1,l):
#     if a[i]>a[j]:
#        a[i],a[j]=a[j],a[i]  
# p=int(input("Enter the position" ))
# if p>l:
#    print("larger than no of elements")    
# else:   
#    print(a[p-1])

#SQAURE
# a=[]
# n=int(input("no:")) 
# for i in range (n):
#     a.append(int(input()))
# b=[]
# for i in a:
#    b.append(i*i)
# print(b)   


# present or not
# a=[]
# n=int(input("no:")) 
# for i in range (n):
#     a.append(int(input()))
# no=int(input("enter a no to search:"))
# j =0
# for i in a:
#     j=j+1
#     if(no==i):
#         j=j+1
#     print("the number",no,"is present in the index of ",j)  
       
   #  else:
   #     print("the number",no,"isn't present")
    
# no of times element is present
# a=[]
# n=int(input("no:")) 
# for i in range (n):
#     a.append(int(input()))
# no=int(input("enter a no to search:"))
# j =0
# for i in a:
    
#     if(no==i):
#         j=j+1
# print("the number",no,"is present ",j,"times") 

# palindrome

# n=int(input("no:")) 
# org=n
# rev=0
# rem=0
# while(n!=0):
#     rem=n%10
#     rev=rev*10 +rem
#     n//=10
   
# if(rev==org) :
#     print("Yes")
# else:
#     print("No")


#  even no in a list
# List=[1,2,3,4,5,6,7,8]
# for x in List:
#     if(x%2 ==0) : 
#         print(x)

# number found or not
# List=[1,2,3,4,5,6,7,8]
# n= int(input("enter a number to search"))
# for x in List:
#     if(n==x):
#         print("found")
#         break
# else:
#     print("not found")

# List=[1,2,3,4,5,6,7,8]
# n= int(input("enter a number to search"))
# l =len(List)
# for i in range(l):
#     if(List[i]==n):
           
#         print("the given number is found in the position of" ,i+1)
#         break
# else:
#     print("not found")
       
# duplicate
# a=[1,2,3,4,1,2,3,4,2]
# l = len(a)
# x= False
# for i in range(l):
#     for j in range(i+1,l):
#         if(a[i]==a[j] ):
#             print(a[i])
#             x=True
#             break
#     if x:
#         break      

# a=[1,2,3,4,1,2,3,4,2]

# for i in a:
#     if a.count(i)>1:
#         print(i)
#         break

# a=[1,2,3,4,5,1]
# b=[]
 
# for i in a:
#     if i in b:
#         print(i)
#         break
#     b.append(i)

# b=[]
# for i in [1,2,3,4,5,2]:
#     if i in b:
#         print(i)
#         break
#     b.append(i)
# else:print("no duplicates found")

# for i in range (10):
#   print(i)    


#ANAGRAM  
# s1='eisten'
# s2='silent'
# a=[]
# b=[]
# if(len(s1)!=len(s2)):
#      print(" NOT AN ANAGRAM")
# else:     
#     for i in s1:
#         a.append(i)
#     for j in s2:
#         b.append(j)
#     a.sort()
#     b.sort()
#     if(a==b):
#         print("ANAGRAM")
    
#     else:
#         print(" NOT AN ANAGRAM")
            
       
# s1='listen'
# s2='silent'
# print("ANAGRAM" if(sorted(s1)== sorted(s2)) else  " NOT AN ANAGRAM")
    
 
# s1='listen'
# s2='silent'
# ls1=[]*26
# ls2=[]*26
# if(len(s1)!=len(s2)):
#        print("NOT ANAGRAM")
# else:     
#    for i in s1.lower():
#       ls1[ord(i)-97]+=1
#    for i in s2.lower():
#       ls2[ord(i)-97]+=1  
#    if(ls1==ls2):
#       print("ANAGRAM")
#    else:
#       print("NOT ANAGRAM")  

s1="kitkat"
ls1=[0]*26
for i in s1.lower():
    ls1[ord(i)-97]+=1
for i in range(len(ls1)):
    if ls1[i]!=0:      
       print(chr(i+97)+str(ls1[i]),end="")    


# s1="aaabbcccc"
# for i in range(len(s1)):
#    for j in range(i+1):
#         s1[i]=












