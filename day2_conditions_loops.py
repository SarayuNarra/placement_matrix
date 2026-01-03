# Program 1: Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ----------------------------

# Program 2: Check positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative or Zero")

# ----------------------------

# Program 3: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# ----------------------------

# Program 4: Sum of first N numbers
n = int(input("Enter N: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum:", sum)

# ----------------------------

# Program 5: Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
