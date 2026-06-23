x=0
y=0
for i in range (100):
  x+=i
  if(i%2==0):
    y+=i
print(x)
print(y)
print(x+y)
print(x==y)

f = int(input("enter a Start value: "))
if (f%2==0):
    s=f
else:
    s=f+1
e = int(input("enter a end value: "))
print(*range(s, e+1, 2))

