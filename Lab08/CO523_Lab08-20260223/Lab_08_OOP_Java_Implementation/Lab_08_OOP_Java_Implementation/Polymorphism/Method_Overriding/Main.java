public class Main {
    public static void main(String[] args) {
        Developer dev = new Developer();
        dev.name = "John";
        dev.id = 3287;
        dev.salary = 65000;

        dev.work();        // Method override
    }
}
