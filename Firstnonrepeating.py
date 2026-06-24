a='swiss'
for i in a:
    if a.count(i)== 1:
        print(i)
        break

a = "swiss"
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1
    if count == 1:
        print(a[i])
        break

a = "swiss"
count = [0] * 26
for ch in a:
    count[ord(ch) - ord('a')] += 1
for ch in a:
    if count[ord(ch) - ord('a')] == 1:
        print(ch)
        break
    