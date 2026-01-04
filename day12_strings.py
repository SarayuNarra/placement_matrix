# Problem 1: Reverse a string
s = input("Enter a string: ")
rev = s[::-1]
print("Reversed string:", rev)

# Problem 2: Check palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Problem 3: Count vowels
s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Vowel count:", count)

# Problem 4: Count character occurrences
s = input("Enter a string: ")
char = input("Enter character to count: ")

print("Occurrences:", s.count(char))

# Problem 5: Remove spaces
s = input("Enter a string: ")
print("Without spaces:", s.replace(" ", ""))
