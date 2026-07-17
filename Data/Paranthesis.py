# str="{{[]}}"
# stack=[]
# for i in str:
#     if i in '{' or i in '(' or i in '[':
#         stack.append(i)
#     else:
#         top=stack.pop()
#         if i == ')' and top!='('  or i=='}' and top!='{' or i=='[' and top!=']':
#             print(False)
#             break
# else:print(True)
 

s = "INDIA IS MY COUNTRY"
vowels = "aeiouAEIOU"
vowel_list = [c for c in s if c in vowels]
reversed_vowels = vowel_list[::-1]
result = []
j = 0
for c in s:
    if c in vowels:
        result.append(reversed_vowels[j])
        j += 1
    else:
        result.append(c)
print("".join(result)) 


# ----------------------------------------------
s = "python is a programing"
vowels = ['a', 'e', 'i', 'o', 'u']
s = list(s)
i = 0
j = len(s) - 1
while i <= j:
    if s[i] not in vowels:
        i += 1
    elif s[j] not in vowels:
        j -= 1
    else:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
print("".join(s))

# -----------------------------------------------------
str ="india is my country"
v=[]
str1=[]
j=0
for i in str:
    if i in 'aeiou':
        v.append(i)
v.reverse()
   
for i in str:
    if i in 'aeiou':
        str1.append(v[j])
        j+=1
    else:
        str1.append(i)
print(''.join(str1))        
 
 
 
 
