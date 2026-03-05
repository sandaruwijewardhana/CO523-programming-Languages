// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Main (Driver Class)
//
// This is the entry point that demonstrates the full real-world OOP scenario.
// It creates the Agent (A1) and LocalTerrorist (L1) objects as specified in the lab,
// then simulates the three weapon purchase cases through the Seller.

public class Main {
    public static void main(String[] args) {
        // Create the agent's service record (A1's initial record as per lab task)
        ServiceRecord recordA1 = new ServiceRecord("Lieutenant", "Captain", 10, 23);

        // Create Agent A1 with the specified attributes
        Agent a1 = new Agent("007", "James bond", 99, recordA1);

        // Create Local Terrorist L1 with the specified attributes
        LocalTerrorist l1 = new LocalTerrorist("John Cobra", "hunter", "Berlin");

        // Create the Seller who controls one bomb and one missile
        Seller seller = new Seller();

        // Print initial agent status before any weapon deals
        System.out.println("=== Initial Agent Status ===");
        a1.printAgentStatus();

        // Case 1: L1 buys the bomb with the correct password — attacks and escapes
        System.out.println("\n=== Case 1: Local Terrorist buys bomb (correct password) ===");
        seller.sellWeapon(l1, a1, "RAPTOR", 1);

        System.out.println("\n=== Agent Status After Bomb Case ===");
        a1.printAgentStatus();

        // Case 2: L1 buys the missile with the correct password — gets caught by agent
        System.out.println("\n=== Case 2: Local Terrorist buys missile (correct password) ===");
        seller.sellWeapon(l1, a1, "RAPTOR", 2);

        System.out.println("\n=== Agent Status After Missile Case ===");
        a1.printAgentStatus();

        // Case 3: Attempt with wrong password — access denied
        System.out.println("\n=== Case 3: Incorrect password ===");
        seller.sellWeapon(l1, a1, "WRONG", 1);
    }
}
