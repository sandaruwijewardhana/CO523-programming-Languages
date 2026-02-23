public class Employee {
    // Private attributes (data is hidden)
    private String name;
    private int id;
    private double salary;

    // Public setter methods (to set values)
    public void setName(String name) {
        this.name = name;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    // Public getter methods (to get values)
    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public double getSalary() {
        return salary;
    }

    // Methods (behaviors)
    public void displayInfo() {
        System.out.println("Name: " + name + ", Salary: $" + salary);
    }

    public void work() {
        System.out.println(name + " is working...");
    }
}

