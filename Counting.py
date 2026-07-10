st="java@!123"
a=0
n=0
s=0
for i in st:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        n+=1
    else:
        s+=1
print("No of character",a,"No of digit",n,"No of Special Characters",s,sep="\n")         


st="java@!123"
a=[0]*3
for i in st:
    if i.isalpha():
        a[0]+=1
    elif i.isdigit():
        a[1]+=1
    else:
        a[2]+=1
# print("No of character",a[0],"No of digit",a[1],"No of Special Characters",a[2],sep="\n")   
print("No of character:", a[0])
print("No of digit:", a[1])
print("No of Special Characters:", a[2])


st="java@!123"
a=0
n=0
s=0
for i in st:
    if i in "q,w,e,r,,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m":
        a+=1
    elif i in "1,2,3,4,5,6,7,8,9,0":
        n+=1
    else:
        s+=1
print("No of character:", a)
print("No of digit:", n)
print("No of Special Characters:", s)

