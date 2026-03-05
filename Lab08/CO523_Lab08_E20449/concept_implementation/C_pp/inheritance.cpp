// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 3.2 - Inheritance
//
// Inheritance enables a class to reuse properties and behaviours of another class.
// It establishes parent (base) and child (derived) class relationships.
// Common logic is defined once and shared across subclasses, reducing redundancy.

#include <iostream>
#include <string>

// Base (parent) class — contains shared attributes and methods
class Employee {
public:
    std::string name;
    int id;
    double salary;

    // Shared method inherited by all derived classes
    void displayInfo() const {
        std::cout << "Name: " << name << ", Salary: $" << salary << '\n';
    }

    // Virtual method — can be overridden by subclasses
    virtual void work() const {
        std::cout << name << " is working..." << '\n';
    }

    virtual ~Employee() = default;
};

// Derived class: Manager inherits from Employee and adds a bonus method
class Manager : public Employee {
public:
    double calculateBonus() const {
        return salary * 0.20;   // Manager gets a 20% bonus
    }
};

// Derived class: Developer inherits from Employee and adds its own bonus method
class Developer : public Employee {
public:
    double calculateBonus() const {
        return salary * 0.10;   // Developer gets a 10% bonus
    }
};

// Derived class: Intern inherits from Employee and adds a learn method
class Intern : public Employee {
public:
    void learn() const {
        std::cout << name << " is learning new skills." << '\n';
    }
};

int main() {
    // Manager object uses inherited displayInfo/work and its own calculateBonus
    Manager mgr;
    mgr.name = "Kevin";
    mgr.id = 1023;
    mgr.salary = 80000;
    mgr.displayInfo();
    mgr.work();
    std::cout << "Manager Bonus: $" << mgr.calculateBonus() << '\n';

    std::cout << '\n';

    Developer dev;
    dev.name = "Bob";
    dev.id = 1012;
    dev.salary = 60000;
    dev.displayInfo();
    dev.work();
    std::cout << "Developer Bonus: $" << dev.calculateBonus() << '\n';

    std::cout << '\n';

    Intern intern;
    intern.name = "Charlie";
    intern.id = 203;
    intern.salary = 20000;
    intern.displayInfo();
    intern.work();
    intern.learn();   // Intern-specific method

    return 0;
}
