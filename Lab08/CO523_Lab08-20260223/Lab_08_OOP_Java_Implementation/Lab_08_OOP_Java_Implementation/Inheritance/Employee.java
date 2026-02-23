public class Employee {
    // Attributes (properties)
    String name;
    int id;
    double salary;
    
    // Methods (behaviors)
    void displayInfo() {
        System.out.println("Name: " + name + ", Salary: $" + salary);
    }
    
    void work() {
        System.out.println(name + " is working...");
    }
}