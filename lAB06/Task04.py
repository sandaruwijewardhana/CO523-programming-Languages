def main():
    print("--- Simple Calculator ---")
    
    while True: # Loop to continue until user exits 
        try:
            # Menu for operations
            print("\nOptions: +, -, *, /, or 'exit' to quit")
            operation = input("Enter operation: ").strip().lower()

            if operation == 'exit':
                print("Exiting calculator. Goodbye!")
                break # Exit the loop [cite: 161, 287]

            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue # Skip to next iteration [cite: 150]

            # Taking numerical inputs
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Expressions for calculations [cite: 14, 293]
            if operation == '+':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif operation == '/':
                # The try-except block will catch division by zero
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")

        except ZeroDivisionError:
            # Handling division by zero [cite: 241, 292]
            print("Error: Cannot divide by zero.")
        except ValueError:
            # Handling invalid input (e.g., entering letters instead of numbers) [cite: 241, 292]
            print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()