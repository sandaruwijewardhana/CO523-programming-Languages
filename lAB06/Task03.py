import sys

def factorial_loop(n):
    """Calculates factorial using a for loop."""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def factorial_recursion(n):
    """Calculates factorial using recursion."""
    if n == 0 or n == 1: # Base case [cite: 173, 197]
        return 1
    return n * factorial_recursion(n - 1) # Recursive case [cite: 174, 199]

def reverse_loop(n):
    """Reverses a number using a while loop."""
    rev = 0
    n = abs(n)
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n //= 10
    return rev

def reverse_recursion(n, rev=0):
    """Reverses a number using recursion."""
    if n == 0: # Base case
        return rev
    return reverse_recursion(n // 10, rev * 10 + n % 10) # Recursive case

def main():
    while True: # Infinite loop for menu repetition [cite: 106, 107]
        print("\n--- Menu ---")
        print("1. Find factorial (loop)")
        print("2. Find factorial (recursion)")
        print("3. Reverse a number (loop)")
        print("4. Reverse a number (recursion)")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ")
            
            if choice == '5':
                print("Exiting program...")
                break # Break statement to exit loop [cite: 161]
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please select 1-5.")
                continue # Skip to next iteration [cite: 150]

            num = int(input("Enter an integer: "))
            
            if choice == '1':
                print(f"Factorial (loop): {factorial_loop(num)}")
            elif choice == '2':
                if num < 0:
                    print("Factorial not defined for negative numbers.")
                else:
                    print(f"Factorial (recursion): {factorial_recursion(num)}")
            elif choice == '3':
                print(f"Reversed (loop): {reverse_loop(num)}")
            elif choice == '4':
                print(f"Reversed (recursion): {reverse_recursion(abs(num))}")
                
        except ValueError as e:
            # Handling invalid input types [cite: 241, 242]
            print(f"Error: Invalid input. {e}")

if __name__ == "__main__":
    main()