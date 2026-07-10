
# ===========================
# 1. Square Pattern
# ===========================
n = int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# ===========================
# 2. Left Triangle
# ===========================
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print("* " * i)

# ===========================
# 3. Right Triangle
# ===========================
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

# ===========================
# 4. Inverted Left Triangle
# ===========================
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print("* " * i)

# ===========================
# 5. Inverted Right Triangle
# ===========================
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

# ===========================
# 6. Pyramid
# ===========================
n = int(input("Enter n: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))

# ===========================
# 7. Diamond
# ===========================
n = int(input("Enter n: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    print("* " * (i + 1))

# ===========================
# 8. Binary Triangle
# ===========================
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()

# ===========================
# 9. Butterfly Pattern
# ===========================
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

# ===========================
# 10. X Pattern
# ===========================
n = int(input("Enter odd n: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ===========================
# 11. Palindrome Triangle
# ===========================
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()

# ===========================
# 12. Sandglass Pattern
# ===========================
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

for i in range(2, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

# ===========================
# 13. Concentric Number Pattern
# ===========================
n = int(input("Enter n: "))
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        value = max(abs(i - (n - 1)), abs(j - (n - 1))) + 1
        print(value, end=" ")
    print()

# ===========================
# 14. Jagged Number Pattern
# ===========================
n = int(input("Enter n: "))

arr = [[0] * (i + 1) for i in range(n)]

num = 1

for i in range(n):
    arr[i][0] = num
    num += 1

for j in range(1, n):
    for i in range(j, n):
        arr[i][j] = num
        num += 1

for row in arr:
    print(*row)
