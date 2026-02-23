public class Employee {
    String name;
    int id;
    double salary;
    
    
    void work() {
        System.out.println(name + " is working...");
    }
	
	void work(String project) {
        System.out.println(name + " is working on project: " + project);
    }
}
