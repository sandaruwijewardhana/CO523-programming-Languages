// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 3.1 - Encapsulation
//
// Encapsulation bundles data and methods that operate on that data within a class.
// The internal state is kept private; access is controlled via public getter/setter methods.
// This ensures data integrity and prevents unauthorized modification.

#include <iostream>
#include <string>

// Employee class with private attributes (data hiding)
class Employee {
private:
    std::string name;   // Hidden from outside — accessed only via getters/setters
    int id;
    double salary;

public:
    // Setter methods — controlled write access to private attributes
    void setName(const std::string& n) { name = n; }
    void setId(int i) { id = i; }
    void setSalary(double s) { salary = s; }

    // Getter methods — controlled read access to private attributes
    std::string getName() const { return name; }
    int getId() const { return id; }
    double getSalary() const { return salary; }

    // Displays employee info using encapsulated private fields
    void displayInfo() const {
        std::cout << "Name: " << name << ", Salary: $" << salary << '\n';
    }

    void work() const {
        std::cout << name << " is working..." << '\n';
    }
};

int main() {
    Employee emp;
    // Modifying private attributes only through setter methods
    emp.setName("Alice");
    emp.setId(101);
    emp.setSalary(50000.0);

    emp.displayInfo();
    emp.work();
    // Accessing private attributes only through getter methods
    std::cout << "Employee Name: " << emp.getName() << '\n';
    std::cout << "Employee Salary: $" << emp.getSalary() << '\n';
    return 0;
}
