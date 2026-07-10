s1 = {2,1, 3, 4}
s2 = {7,8,0,1,9, 3, 5}
r = s1.union(s2)
print("Union:", r)
r1 = s1.difference(s2)
print("Difference (s1 - s2):", r1)
r2 = s1.intersection(s2)
print("Intersection:", r2)
r3 = s1.copy()
print("Copy:", r3)
s1.add(6)
print("After add(6):", s1)
s1.update([6, 7, 9])
print("After update([6, 7, 9]):", s1)
s1.difference_update(s2)
print("After difference_update(s2):", s1)
s1 = {1, 3, 4}
s1.intersection_update(s2)
print("After intersection_update(s2):", s1)


