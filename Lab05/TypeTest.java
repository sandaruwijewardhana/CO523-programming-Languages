public class TypeTest {
    public static void main(String[] args) {
        int a = 10;
        String b = "5";
        double c = 2.5;

        // 1. Explicitly converting String to Integer for mathematical addition
        int r1 = a + Integer.parseInt(b); 
        System.out.println("Mathematical Addition (int + parsed string): " + r1);

        // 2. Explicitly casting double to int (Narrowing Conversion - loses precision)
        int r2 = a + (int)c; 
        System.out.println("Addition with Explicit Cast (int + (int)double): " + r2);

        // 3. Explicitly converting all to String
        String r3 = String.valueOf(a) + b + String.valueOf(c);
        System.out.println("Explicit String Concatenation: " + r3);

        // 4. Implicit Widening (int promoted to double)
        double r5 = a + c;
        System.out.println("Implicit Widening (int + double): " + r5);
    }
}