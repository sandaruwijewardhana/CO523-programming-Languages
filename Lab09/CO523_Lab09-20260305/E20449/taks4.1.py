# Task 4.1: Pure Function - Average Calculation
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    This is a pure function:
    1. It produces the same output for the same input.
    2. It has no side effects.
    """
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

# Verification
if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50]

    # Call the function multiple times with the same input 
    result_1 = calculate_average(test_list)
    result_2 = calculate_average(test_list)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")
    
    # Verify identical output 
    print(f"Identical: {result_1 == result_2}")
    
    # Verify original list remains unmodified 
    print(f"Original list safe: {test_list}")