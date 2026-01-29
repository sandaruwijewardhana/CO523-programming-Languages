def infinite_recursion():
    """A recursive function with no base case."""
    print("Calling function...")
    # Recursive Case: Function calls itself without a stopping condition
    return infinite_recursion()

# Executing the function
try:
    infinite_recursion()
except RecursionError as e:
    print(f"\nResult: {e}")