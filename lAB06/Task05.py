def infinite_recursion():
    """A recursive function with no base case."""
    print("Calling function...")
   
    return infinite_recursion()
try:
    infinite_recursion()
except RecursionError as e:
    print(f"\nResult: {e}")