public class Main {
    public static void main(String[] args) {

        // Manager object
        Manager mgr = new Manager();
        mgr.name = "Kevin";
        mgr.id = 1023;
        mgr.salary = 80000;
        mgr.displayInfo();
        mgr.work();
        System.out.println("Manager Bonus: $" + mgr.calculateBonus());

        System.out.println();

        // Developer object
        Developer dev = new Developer();
        dev.name = "Bob";
        dev.id = 1012;
        dev.salary = 60000;
        dev.displayInfo();
        dev.work();
        System.out.println("Manager Bonus: $" + mgr.calculateBonus());
        System.out.println();

        // Intern object
        Intern intern = new Intern();
        intern.name = "Charlie";
        intern.id = 203;
        intern.salary = 20000;
        intern.displayInfo();
        intern.work();
        intern.learn();
    }
}
