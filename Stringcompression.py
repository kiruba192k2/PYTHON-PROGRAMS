s1="kitkat"
ls1=[0]*26
for i in s1.lower():
    ls1[ord(i)-97]+=1
for i in range(len(ls1)):
    if ls1[i]!=0:      
       print(chr(i+97)+str(ls1[i]),end="")    


s1="kirubanidhi"
a=[]
ct =[]
for i in s1:
    if i in a:
        index=a.index(i)
        ct[index]+=1
        
    else:
        a.append(i)
        ct.append(1)

for j in range(len(a)):
  print(str(a[j])+str(ct[j]),end="") 










