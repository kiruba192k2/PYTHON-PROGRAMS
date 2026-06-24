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