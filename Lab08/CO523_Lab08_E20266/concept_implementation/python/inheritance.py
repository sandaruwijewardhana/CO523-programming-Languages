# CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
# Section 3.2 - Inheritance
#
# Inheritance enables a class to reuse properties and behaviours of another class.
# Manager, Developer, and Intern all inherit shared attributes and methods from Employee,
# while each adds its own specialized behavior.

class Employee:
    def __init__(self):
        # Shared attributes inherited by all subclasses
        self.name = ""
        self.id = 0
        self.salary = 0.0

    # Shared method — available to all subclasses
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")

    def work(self):
        print(f"{self.name} is working...")


# Derived class: Manager inherits Employee and adds a bonus calculation method
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20   # Manager gets a 20% bonus


# Derived class: Developer inherits Employee and adds its own bonus calculation
class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10   # Developer gets a 10% bonus


# Derived class: Intern inherits Employee and adds a learn method
class Intern(Employee):
    def learn(self):
        print(f"{self.name} is learning new skills.")


def main():
    # Manager uses inherited display_info/work and its own calculate_bonus
    mgr = Manager()
    mgr.name = "Kevin"
    mgr.id = 1023
    mgr.salary = 80000
    mgr.display_info()
    mgr.work()
    print(f"Manager Bonus: ${mgr.calculate_bonus()}")

    print()

    dev = Developer()
    dev.name = "Bob"
    dev.id = 1012
    dev.salary = 60000
    dev.display_info()
    dev.work()
    print(f"Developer Bonus: ${dev.calculate_bonus()}")

    print()

    intern = Intern()
    intern.name = "Charlie"
    intern.id = 203
    intern.salary = 20000
    intern.display_info()
    intern.work()
    intern.learn()   # Intern-specific method


if __name__ == "__main__":
    main()
