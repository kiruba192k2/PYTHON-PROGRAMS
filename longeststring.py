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

stream = 'Java is a powerful language'
largest = 0
result = ''

for i in stream.split():
    iLength = len(i)
    if iLength > largest:
        largest = iLength
        result = i

print(result)


str= 'Java is a powerful language'
largest = currentLength = 0
result = currentWord = ''

for i in str + ' ':
    if i == ' ':
        if currentLength > largest:
            result = currentWord
            largest = currentLength
        currentWord = ''
        currentLength = 0
    else:
        currentLength += 1
        currentWord += i

print(result)
        