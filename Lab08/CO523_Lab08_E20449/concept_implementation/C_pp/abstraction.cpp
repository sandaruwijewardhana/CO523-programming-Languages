// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 3.3 - Abstraction
//
// Abstraction exposes only essential features of an object while hiding internal details.
// Abstract classes define what an object should do (the interface), not how it does it.
// Concrete subclasses provide the actual implementation of abstract methods.

#include <iostream>
#include <string>

// Abstract base class — defines the interface but cannot be instantiated directly
class Employee {
public:
    std::string name;
    int id;
    double salary;

    // Pure virtual method — subclasses MUST implement their own version of work()
    virtual void work() const = 0;

    // Concrete method — shared by all subclasses without modification
    void displayInfo() const {
        std::cout << "Name: " << name << ", Salary: $" << salary << '\n';
    }

    virtual ~Employee() = default;
};

// Concrete class: Developer provides its own implementation of the abstract work()
class Developer : public Employee {
public:
    void work() const override {
        std::cout << name << " is writing code." << '\n';
    }
};

// Concrete class: Manager provides its own implementation of the abstract work()
class Manager : public Employee {
public:
    void work() const override {
        std::cout << name << " is managing the team." << '\n';
    }
};

int main() {
    // Using Developer object — abstract work() implemented in this subclass
    Developer dev;
    dev.name = "Tom";
    dev.id = 2157;
    dev.salary = 60000;
    dev.displayInfo();   // Concrete method called directly
    dev.work();          // Abstract method implemented in Developer

    Manager mgr;
    mgr.name = "Billy";
    mgr.id = 3015;
    mgr.salary = 85000;
    mgr.displayInfo();
    mgr.work();

    return 0;
}
