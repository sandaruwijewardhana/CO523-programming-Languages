def factorial_recursive(n):
    """Calculates factorial using recursion."""
    # Base Case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive Case: n * factorial of (n-1)
    return n * factorial_recursive(n - 1)

def sum_of_digits_loop(n):
    """Calculates sum of digits using a loop."""
    n = abs(n)  # Convert to positive to handle digits correctly
    total_sum = 0
    while n > 0:
        total_sum += n % 10  # Get the last digit
        n //= 10             # Remove the last digit
    return total_sum

def main():
    try:
        # Taking integer input
        user_input = input("Enter an integer: ")
        num = int(user_input)

        if num > 0:
            # If positive, find factorial using recursion
            result = factorial_recursive(num)
            print(f"The number is positive. Factorial of {num} is: {result}")
        
        elif num < 0:
            # If negative, find sum of digits using a loop
            result = sum_of_digits_loop(num)
            print(f"The number is negative. Sum of its digits is: {result}")
        
        else:
            # If zero
            print("The number is zero.")

    except ValueError:
        # Exception handling for invalid (non-integer) input
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()