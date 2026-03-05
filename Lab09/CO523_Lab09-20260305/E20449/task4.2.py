# Task 4.2: Higher-Order Function Implementation

# 1. Higher-order function that takes a function and a value
def apply_twice(func, x):
    """Applies the passed function 'func' to 'x' twice."""
    return func(func(x))

# 2. Function to square a number
def square(x):
    return x * x

# 3. Function to increment a number
def increment(x):
    return x + 1

# Testing and Verification
if __name__ == "__main__":
    
    # Expected behavior: apply_twice(square, 2) -> square(square(2)) -> square(4) -> 16
    res_square = apply_twice(square, 2)
    print(f"apply_twice(square, 2) = {res_square}") # Output: 16

    # Expected behavior: apply_twice(increment, 5) -> increment(increment(5)) -> increment(6) -> 7
    res_increment = apply_twice(increment, 5)
    print(f"apply_twice(increment, 5) = {res_increment}") # Output: 7