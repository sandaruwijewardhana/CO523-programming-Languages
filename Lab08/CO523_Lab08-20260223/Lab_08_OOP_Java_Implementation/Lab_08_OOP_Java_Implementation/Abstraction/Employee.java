abstract class Employee {
    protected String name;   // Variable in abstract class
    protected int id;        // Variable in abstract class
    protected double salary; // Variable in abstract class

    // Abstract method → no body, must be implemented by subclasses
    abstract void work();

    // Concrete method → shared by all
    void displayInfo() {
        System.out.println("Name: " + name + ", Salary: $" + salary);
    }
}
