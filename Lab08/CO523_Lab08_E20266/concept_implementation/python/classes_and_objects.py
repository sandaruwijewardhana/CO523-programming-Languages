# CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
# Section 2.2 - Classes and Objects
#
# A class is a blueprint for creating objects.
# It defines attributes (properties) and methods (behaviors).
# An object is an instance of a class with specifically defined data.

class Employee:
    def __init__(self):
        # Attributes: store the state of the Employee object
        self.name = ""
        self.id = 0
        self.salary = 0.0

    # Method: prints the employee's name and salary
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

    # Method: prints a generic work message
    def work(self):
        print(f"{self.name} is working...")


def main():
    # Creating an object (instance) of the Employee class
    emp = Employee()
    emp.name = "Alice"      # Setting the name
    emp.id = 101            # Setting the ID
    emp.salary = 50000.0    # Setting the salary

    emp.display_info()                          # Calling the display_info method
    emp.work()                                  # Calling the work method
    print(f"Employee Name: {emp.name}")         # Accessing attribute directly


if __name__ == "__main__":
    main()
