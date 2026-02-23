public class Main {
    public static void main(String[] args) {
        Developer dev = new Developer();
        dev.name = "Tom";
        dev.id = 2157;
        dev.salary = 60000;

        dev.displayInfo(); // Concrete method
        dev.work();        // Concrete method

        Manager mgr = new Manager();
        mgr.name = "Billy";
        mgr.id = 3015;
        mgr.salary = 85000;

        mgr.displayInfo(); // Concrete method
        mgr.work();        // Concrete method
    }
}