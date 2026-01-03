# Program 1: Add two numbers
def add(a, b):
    return a + b

print(add(10, 20))

# ----------------------------

# Program 2: Check even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(7))

# ----------------------------

# Program 3: Find maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(5, 9))

# ----------------------------

# Program 4: Calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

# ----------------------------

# Program 5: Simple Interest
def simple_interest(p, t, r):
    return (p * t * r) / 100

print(simple_interest(1000, 2, 5))
