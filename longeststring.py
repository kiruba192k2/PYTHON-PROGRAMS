# First longest string
s="Java is the powerful language"
a=s.split()
print(a)
l=""
for i in range(len(a)):
   
        if(len(a[i])>len(l)):
            l=a[i]
print(l)  

# Longest String
s="Java is the powerful language"
a=s.split()
print(a)
l=0
for i in range(len(a)):   
        if(len(a[i])>l):
            l=len(a[i])
for i in range(len(a)):
     if(len(a[i])==l):
        print(a[i])            


        