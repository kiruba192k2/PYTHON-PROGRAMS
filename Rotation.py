str1 = "ABCD"
str2 = "CDAB"
t = ""
for i in range(len(str1)):
    if str1 +t  == str2:
        print(True)
        quit()
    t += str1[0]
    str1 = str1[1:]
else:
    print(False)


# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")

# if len(string1) == len(string2) and string2 in (string1 + string1):
#     print("Rotation")
# else:
#     print("Not Rotation")