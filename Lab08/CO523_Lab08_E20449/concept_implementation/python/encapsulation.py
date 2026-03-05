# CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
# Section 3.1 - Encapsulation
#
# Encapsulation bundles data and methods within a class.
# The internal state is kept private (prefixed with __), accessed only via
# public getter and setter methods to ensure data integrity.

class Employee:
    def __init__(self):
        # Private attributes — name-mangled to prevent direct external access
        self.__name = ""
        self.__id = 0
        self.__salary = 0.0

    # Setter methods — controlled write access to private attributes
    def set_name(self, name):
        self.__name = name

    def set_id(self, emp_id):
        self.__id = emp_id

    def set_salary(self, salary):
        self.__salary = salary

    # Getter methods — controlled read access to private attributes
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_salary(self):
        return self.__salary

    # Method: displays employee info using private fields internally
    def display_info(self):
        print(f"Name: {self.__name}, Salary: ${self.__salary}")

    def work(self):
        print(f"{self.__name} is working...")


def main():
    emp = Employee()
    # Modify private attributes only through setter methods
    emp.set_name("Alice")
    emp.set_id(101)
    emp.set_salary(50000.0)

    emp.display_info()
    emp.work()
    # Access private attributes only through getter methods
    print(f"Employee Name: {emp.get_name()}")
    print(f"Employee Salary: ${emp.get_salary()}")


if __name__ == "__main__":
    main()
