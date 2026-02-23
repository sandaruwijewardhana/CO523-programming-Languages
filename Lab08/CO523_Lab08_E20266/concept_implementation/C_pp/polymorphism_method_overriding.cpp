// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 3.4.2 - Runtime Polymorphism (Method Overriding)
//
// Method overriding allows a subclass to provide a specific implementation
// for a method already defined in the superclass. The correct implementation
// is resolved at runtime based on the actual object type.

#include <iostream>
#include <string>

// Base class — defines a virtual work() method that can be overridden
class Employee {
public:
    std::string name;
    int id;
    double salary;

    virtual void work() const {
        std::cout << name << " is working..." << '\n';
    }

    virtual ~Employee() = default;
};

// Derived class — overrides work() with Developer-specific behavior
class Developer : public Employee {
public:
    void work() const override {
        std::cout << name << " is writing code." << '\n';
    }
};

int main() {
    Developer dev;
    dev.name = "John";
    dev.id = 3287;
    dev.salary = 65000;
    dev.work();   // Calls Developer's overridden work(), not Employee's base version

    return 0;
}
