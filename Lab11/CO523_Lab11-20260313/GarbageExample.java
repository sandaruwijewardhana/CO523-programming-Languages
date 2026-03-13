// Student class with a finalize method to observe cleanup
class Student {
    String name;

    Student(String name) {
        this.name = name;
        System.out.println("Student object '" + this.name + "' created in heap.");
    }

    // This method is called by the GC before destroying the object
    @Override
    protected void finalize() throws Throwable {
        System.out.println("Garbage Collector is removing '" + this.name + "'.");
    }
}

public class GarbageExample {
    public static void main(String[] args) {
        // 1. Create at least three objects
        Student s1 = new Student("Kamal"); 
        Student s2 = new Student("Nimal");
        Student s3 = new Student("Sunil");

        // 2. Remove references to one or two objects using null
        System.out.println("\n--- Setting s1 and s2 to null ---");
        s1 = null; // s1 becomes eligible for GC 
        s2 = null; // s2 becomes eligible for GC 

        // 3. Call System.gc()
        System.out.println("--- Requesting Garbage Collection ---");
        System.gc(); // Request JVM to run garbage collector 

        // Brief delay to allow GC thread to run
        try { Thread.sleep(1000); } catch (InterruptedException e) {}

        System.out.println("\n--- End of main method ---");
    }
}