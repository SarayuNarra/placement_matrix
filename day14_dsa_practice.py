# Day 14: DSA Practice Problems

# Problem 1: Find maximum element in a list
arr = [10, 25, 5, 40, 30]
print("Maximum element:", max(arr))


# Problem 2: Find minimum element in a list
print("Minimum element:", min(arr))


# Problem 3: Linear search
key = 40
found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")


# Problem 4: Find sum of elements in an array
total = 0
for num in arr:
    total += num

print("Sum of elements:", total)


# Problem 5: Find second largest element in an array
unique_arr = list(set(arr))
unique_arr.sort(reverse=True)

if len(unique_arr) >= 2:
    print("Second largest element:", unique_arr[1])
else:
    print("No second largest element")
