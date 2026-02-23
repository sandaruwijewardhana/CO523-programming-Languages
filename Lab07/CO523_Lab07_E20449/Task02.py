# Task 02 - Python (pass-by-reference simulation using mutable list)

def modify_list(lst):
    lst[0] = lst[0] + 10
    print("Inside function:", lst)

numbers = [int(input("Enter an integer: "))]
print("Before function:", numbers)

modify_list(numbers)

print("After function:", numbers)