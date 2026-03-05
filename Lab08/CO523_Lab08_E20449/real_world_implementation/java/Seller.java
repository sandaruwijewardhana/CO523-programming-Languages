// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Seller (Encapsulation + Polymorphism)
//
// The Seller owns one Bomb (b1) and one Missile (m1) and controls access via a password.
// Polymorphism: sellWeapon accepts a Terrorist type variable — both LocalTerrorist and
// GlobalTerrorist objects can be passed, and the correct overridden methods are called.

public class Seller {
    private static final String PASSWORD = "RAPTOR"; // Password required to buy a weapon

    // Pre-created weapons available for sale (per Lab Task 4.3, Part C)
    private final Bomb b1;
    private final Missile m1;

    public Seller() {
        b1 = new Bomb("Clemo", 12.00f); // Bomb b1 attributes
        m1 = new Missile("0001", "Intercontinental", "nuclear"); // Missile m1 attributes
    }

    // sellWeapon — handles the full weapon purchase procedure as specified in the
    // lab
    public void sellWeapon(Terrorist terrorist, Agent agent, String password, int weaponChoice) {
        // Verify password before allowing the weapon sale
        if (!PASSWORD.equals(password)) {
            System.out.println("Access denied. Incorrect password.");
            return;
        }

        if (weaponChoice == 1) {
            // Terrorist buys the bomb, attacks, and escapes
            System.out.println("Bomb selected: " + b1.getCategory());
            terrorist.buyWeapon(b1); // Calls deploy() on the bomb
            terrorist.attack();
            System.out.println("Terrorist escaped after bomb attack.");
        } else if (weaponChoice == 2) {
            // Terrorist buys the missile but is caught; agent gains promotion and
            // experience
            System.out.println("Missile selected: " + m1.getCode() + ", " + m1.getRange() + ", " + m1.getType());
            terrorist.buyWeapon(m1); // Calls deploy() on the missile
            agent.catchTerrorist(terrorist);
            agent.promote("Major"); // Agent is promoted after successful capture
            agent.missionSuccess(); // Mission count incremented
            agent.addExperience(); // Years of service incremented
            System.out.println("Agent record updated after successful capture.");
        } else {
            System.out.println("Invalid weapon selection.");
        }
    }
}
