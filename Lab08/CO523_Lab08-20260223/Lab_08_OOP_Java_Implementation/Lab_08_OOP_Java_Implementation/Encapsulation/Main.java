public class Main {
    public static void main(String[] args) {
        // Creating an object of the Employee class
        Employee emp = new Employee();

        // Setting values using setter methods
        emp.setName("Alice");
        emp.setId(101);
        emp.setSalary(50000.0);

        // Calling methods
        emp.displayInfo();   // Output: Name: Alice, Salary: $50000.0
        emp.work();          // Output: Alice is working...

        // Accessing values using getter methods
        System.out.println("Employee Name: " + emp.getName());
        System.out.println("Employee Salary: $" + emp.getSalary());
    }
}
