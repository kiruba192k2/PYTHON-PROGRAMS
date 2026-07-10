
a = "aaababbcdddjbjbvjvjv"
freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

s = ''.join(sorted(a))
print(s)


dict = {"John": 20, "Mary": 21, "Tom": 20, "Alice": 21}

group= {}

for i in dict:
    if dict[i] in grouped:
        group[dict[i]].append(i)
    else:
        group[dict[i]] = [i]

print(group)


