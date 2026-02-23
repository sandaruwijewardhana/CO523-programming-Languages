public class Main {
    public static void main(String[] args) {
        Employee emp = new Employee();
        emp.name = "Jeorge";
		emp.id = 1452;
		emp.salary = 71000;

        emp.work();                 // Output: Jeorge is working.
        emp.work("Website Redesign"); // Output: Jeorge is working on project: Website Redesign
    }
}
