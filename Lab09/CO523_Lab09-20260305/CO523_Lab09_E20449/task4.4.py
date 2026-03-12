# Task 4.4: Recursion Practice

# 1. Fibonacci Implementation
def fibonacci(n):
    # Base cases
    if n <= 0: return 0
    if n == 1: return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# 2. Reverse a String
def reverse_string(s):
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive case: last character + reverse of the rest
    return s[-1] + reverse_string(s[:-1])

# 3. Find maximum element in a list
def find_max(lst):
    # Base case: single element
    if len(lst) == 1:
        return lst[0]
    # Recursive case: compare first element with max of the rest
    sub_max = find_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

# Verification
if __name__ == "__main__":
    print(f"Fibonacci(6): {fibonacci(6)}")# Output: 8
    print(f"Reverse 'CO523': {reverse_string('CO523')}")# Output: 325OC
    print(f"Max of [3, 1, 9, 2]: {find_max([3, 1, 9, 2])}")# Output: 9