// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 3.4.1 - Compile-time Polymorphism (Method Overloading)
//
// Method overloading allows a class to have multiple methods with the same name
// but different parameter lists. The correct method is chosen at compile time
// based on the number and type of arguments passed.

#include <iostream>
#include <string>

class Employee {
public:
    std::string name;
    int id;
    double salary;

    // Overload 1: work() with no arguments — general work message
    void work() const {
        std::cout << name << " is working..." << '\n';
    }

    // Overload 2: work(project) — specific work message with a project name
    void work(const std::string& project) const {
        std::cout << name << " is working on project: " << project << '\n';
    }
};

int main() {
    Employee emp;
    emp.name = "Jeorge";
    emp.id = 1452;
    emp.salary = 71000;

    emp.work();                    // Calls overload 1 — no argument
    emp.work("Website Redesign");  // Calls overload 2 — string argument

    return 0;
}
