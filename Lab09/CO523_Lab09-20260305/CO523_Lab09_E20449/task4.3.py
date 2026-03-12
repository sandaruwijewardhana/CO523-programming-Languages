from functools import reduce

# Task 4.3: Functional Data Pipeline
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. Filter even numbers
evens = filter(lambda x: x % 2 == 0, nums)

# 2. Square the filtered numbers
squares = map(lambda x: x ** 2, evens)

# 3. Find the sum using reduce
total_sum = reduce(lambda x, y: x + y, squares)

# Expected output: 4^2 + 6^2 + 8^2 = 16 + 36 + 64 = 116
print(f"Result: {total_sum}")
