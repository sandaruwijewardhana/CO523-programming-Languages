# Task 01 - Python (pass-by-value behavior with immutable int)

def modify(x):
    x = x + 10
    print("Inside function:", x)

a = int(input("Enter an integer: "))
print("Before function:", a)

modify(a)

print("After function:", a)