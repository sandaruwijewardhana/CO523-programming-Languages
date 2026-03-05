// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 2.2 - Classes and Objects
//
// A class is a blueprint for creating objects.
// It defines attributes (properties) and methods (behaviors).
// An object is an instance of a class with specifically defined data.

#include <iostream>
#include <string>

// Employee class — defines attributes and behaviors of an employee
class Employee {
public:
    std::string name;   // Attribute: employee name
    int id;             // Attribute: employee ID
    double salary;      // Attribute: employee salary

    // Method: prints the employee's name and salary
    void displayInfo() const {
        std::cout << "Name: " << name << ", Salary: $" << salary << '\n';
    }

    // Method: prints a generic work message
    void work() const {
        std::cout << name << " is working..." << '\n';
    }
};

int main() {
    // Creating an object (instance) of the Employee class
    Employee emp;
    emp.name = "Alice";       // Setting the name
    emp.id = 101;             // Setting the ID
    emp.salary = 50000.0;     // Setting the salary

    emp.displayInfo();        // Calling the displayInfo method
    emp.work();               // Calling the work method
    std::cout << "Employee Name: " << emp.name << '\n';
    return 0;
}
