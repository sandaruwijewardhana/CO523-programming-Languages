public class Main {
    public static void main(String[] args) {
        ServiceRecord recordA1 = new ServiceRecord("Lieutenant", "Captain", 10, 23);
        Agent a1 = new Agent("007", "James bond", 99, recordA1);

        LocalTerrorist l1 = new LocalTerrorist("John Cobra", "hunter", "Berlin");

        Seller seller = new Seller();

        System.out.println("=== Initial Agent Status ===");
        a1.printAgentStatus();

        System.out.println("\n=== Case 1: Local Terrorist buys bomb (correct password) ===");
        seller.sellWeapon(l1, a1, "RAPTOR", 1);

        System.out.println("\n=== Agent Status After Bomb Case ===");
        a1.printAgentStatus();

        System.out.println("\n=== Case 2: Local Terrorist buys missile (correct password) ===");
        seller.sellWeapon(l1, a1, "RAPTOR", 2);

        System.out.println("\n=== Agent Status After Missile Case ===");
        a1.printAgentStatus();

        System.out.println("\n=== Case 3: Incorrect password ===");
        seller.sellWeapon(l1, a1, "WRONG", 1);
    }
}
