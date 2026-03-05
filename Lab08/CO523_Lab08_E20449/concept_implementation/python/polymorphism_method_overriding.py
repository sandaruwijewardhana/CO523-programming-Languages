# CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
# Section 3.4.2 - Runtime Polymorphism (Method Overriding)
#
# Method overriding allows a subclass to provide its own implementation
# for a method already defined in the parent class.
# The overridden version is called at runtime based on the actual object type.

class Employee:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.salary = 0.0

    # Base version of work() — can be overridden by subclasses
    def work(self):
        print(f"{self.name} is working...")


# Developer overrides work() with its own developer-specific behavior
class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")   # Overrides parent's work()


def main():
    dev = Developer()
    dev.name = "John"
    dev.id = 3287
    dev.salary = 65000

    dev.work()   # Calls Developer's overridden work(), not the base Employee version


if __name__ == "__main__":
    main()
