def power_recursive(base, exponent):
    """Calculates base raised to the power of exponent using recursion."""
    # Base Case: Any number raised to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive Case: base * (base ^ (exponent - 1))
    return base * power_recursive(base, exponent - 1)

def main():
    try:
        # Taking number n as input
        n = int(input("Enter a number (n): "))

        print("\n--- Number Pattern ---")
        # Outer loop for rows from 1 up to n
        for i in range(1, n + 1):
            # Inner loop for numbers in each row
            for j in range(1, i + 1):
                print(j, end="")
            # Move to next line after inner loop completes
            print()

        # Calculate n^5 using recursion
        power_result = power_recursive(n, 5)
        print(f"\n{n} raised to the power 5 is: {power_result}")

    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()