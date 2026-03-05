# CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
# Section 3.3 - Abstraction
#
# Abstraction exposes only essential features of an object, hiding implementation details.
# The ABC module provides the tools to create abstract base classes in Python.
# Subclasses must implement any method marked with @abstractmethod.

from abc import ABC, abstractmethod


# Abstract base class — defines the interface, cannot be instantiated directly
class Employee(ABC):
    def __init__(self):
        # Shared attributes available to all concrete subclasses
        self.name = ""
        self.id = 0
        self.salary = 0.0

    # Abstract method — each subclass must provide its own work() implementation
    @abstractmethod
    def work(self):
        pass

    # Concrete method — shared by all subclasses without modification
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")


# Concrete subclass: Developer implements the abstract work() method
class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")


# Concrete subclass: Manager implements the abstract work() method
class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team.")


def main():
    dev = Developer()
    dev.name = "Tom"
    dev.id = 2157
    dev.salary = 60000

    dev.display_info()   # Concrete method used directly
    dev.work()           # Abstract method implemented in Developer

    mgr = Manager()
    mgr.name = "Billy"
    mgr.id = 3015
    mgr.salary = 85000

    mgr.display_info()
    mgr.work()


if __name__ == "__main__":
    main()
