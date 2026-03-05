# CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
# Section 3.4.1 - Compile-time Polymorphism (Method Overloading)
#
# Python does not natively support method overloading, but the same effect is achieved
# using a default parameter (project=None). The method behaves differently based on
# whether a project name is passed or not.

class Employee:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.salary = 0.0

    # Single method simulating overloading via an optional parameter
    def work(self, project=None):
        if project is None:
            # No argument — general work message (simulates overload 1)
            print(f"{self.name} is working...")
        else:
            # Project argument given — specific work message (simulates overload 2)
            print(f"{self.name} is working on project: {project}")


def main():
    emp = Employee()
    emp.name = "Jeorge"
    emp.id = 1452
    emp.salary = 71000

    emp.work()                    # Called without argument
    emp.work("Website Redesign")  # Called with a project argument


if __name__ == "__main__":
    main()
