public class Main {
    public static void main(String[] args) {
        // Creating an object of the Employee class
        Employee emp = new Employee();
        emp.name = "Alice";     // Setting the name
        emp.id = 101;           // Setting the ID
        emp.salary = 50000.0;   // Setting the salary
        
        // Calling methods on the object
        emp.displayInfo();  // Output: Name: Alice, Salary: $50000.0
        emp.work();         // Output: Alice is working...
        
        // Accessing fields directly
        System.out.println("Employee Name: " + emp.name);  // Output: Employee Name: Alice
    }
}
