s1='eisten'
s2='silent'
a=[]
b=[]
if(len(s1)!=len(s2)):
     print(" NOT AN ANAGRAM")
else:     
    for i in s1:
        a.append(i)
    for j in s2:
        b.append(j)
    a.sort()
    b.sort()
    if(a==b):
        print("ANAGRAM")
    
    else:
        print(" NOT AN ANAGRAM")
            
       
s1='listen'
s2='silent'
print("ANAGRAM" if(sorted(s1)== sorted(s2)) else  " NOT AN ANAGRAM")
    
 
s1='listen'
s2='silent'
ls1=[]*26
ls2=[]*26
if(len(s1)!=len(s2)):
       print("NOT ANAGRAM")
else:     
   for i in s1.lower():
      ls1[ord(i)-97]+=1
   for i in s2.lower():
      ls2[ord(i)-97]+=1  
   if(ls1==ls2):
      print("ANAGRAM")
   else:
      print("NOT ANAGRAM") 