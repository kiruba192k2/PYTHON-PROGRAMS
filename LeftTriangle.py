n = int(input())
for i in range(1,n+1):
    temp=""
    for j in range(1,i+1):
        if i==n or j==i or j==1 :
            temp+="* "
        else:
            temp+="  "

    print(temp[:-1])


