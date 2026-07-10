s = input("Enter a string: ")
a =s
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
s=sorted(freq,key=lambda x:freq[x])
result = ones = ''
for i in s[::-1]:
    frequency = freq[i]
    half = frequency // 2
    if frequency % 2 and not ones:
        result += i * half
        ones = i
    elif frequency > 1:
        result += i * half
largestPalindrome = result + ones + result[::-1]
print(largestPalindrome)
print(len(largestPalindrome))
print(largestPalindrome == largestPalindrome[::-1])
print("------------------------------------------------")
freq = {}
for ch in a:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
middle = ""
for ch in sorted(freq.keys(), reverse=True):
    if freq[ch] % 2 == 1:
        middle = ch
        freq[ch] -= 1       
        break
palindrome = middle
for ch in sorted(freq.keys(), reverse=True):
    if freq[ch] > 0:
        half = freq[ch] // 2
        if half > 0:
            palindrome = (ch * half) + palindrome + (ch * half)
print("Largest Palindrome:", palindrome)
print(len(palindrome))
print("Is Palindrome:", palindrome == palindrome[::-1])

# Word Pattern : pattern="abba" , sentence="dog cat cat dog" . O/P : True.
'''
pattern = "abba"
sentence = "dog cat cat dog"

words = sentence.split()

stream = {}

for i in range(len(pattern)):
    currentWord, currentMatch = pattern[i], words[i]

    if currentWord in stream and stream[currentWord] != currentMatch:
        print(False)
        quit()

    stream[currentWord] = currentMatch

print(True)
'''